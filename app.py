import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import PGVector
from langchain.embeddings import HuggingFaceEmbeddings


load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"use_auth_token": os.getenv("HF_TOKEN")}
)

CONNECTION_STRING = os.getenv('NEON_DB_URL')
COLLECTION_NAME = "pdf_documents"


st.title("PDF QA Assistant")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name
    
    if st.button("Process PDF"):
        try:
            # Load and split PDF
            loader = PyPDFLoader(tmp_path)
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=100,
                separators=["\n\n", "\n", " ", ""]
            )
            chunks = text_splitter.split_documents(docs)
            
            # Store embeddings in Neon
            PGVector.from_documents(
                documents=chunks,
                embedding=embeddings,
                collection_name=COLLECTION_NAME,
                connection_string=CONNECTION_STRING,
            )
            st.success("PDF processed successfully!")
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
        finally:
            os.unlink(tmp_path)


question = st.text_input("Ask a question about the PDF")
if question:
    try:
        
        db = PGVector(
            collection_name=COLLECTION_NAME,
            connection_string=CONNECTION_STRING,
            embedding_function=embeddings,
        )
        
        
        docs = db.similarity_search(question, k=3)
        
        st.subheader("Most Relevant Answers:")
        for i, doc in enumerate(docs, 1):
            st.write(f"**Answer {i}:** {doc.page_content}")
    except Exception as e:
        st.error(f"Error retrieving answers: {e}")

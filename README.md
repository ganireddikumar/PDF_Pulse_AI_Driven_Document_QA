# A simple app that answers questions from PDFs using AI.

## Tools Used
- Streamlit (Web interface)

- Hugging Face (Text embeddings)

- Neon.tech (Free PostgreSQL database)

- LangChain (PDF processing)

## Setup
- Get Free Accounts

- Create a Neon.tech database

- Get a Hugging Face token (free)


## Create requirements.txt:



- streamlit
- langchain
- psycopg2-binary
- pypdf
- python-dotenv
- langchain-community
- sentence-transformers



## Add Secrets

## Design Choices
- Free Database: Neon.tech for zero-cost PostgreSQL

- Simple Chunks: 500-character text splits for basic context

- Lightweight AI: Small embedding model to save resources

## How It Works

- Upload PDF → 2. Split text → 3. Save to database → 4. Ask questions → 5. Get answers

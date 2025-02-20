A simple app that answers questions from PDFs using AI.

Tools Used
Streamlit (Web interface)

Hugging Face (Text embeddings)

Neon.tech (Free PostgreSQL database)

LangChain (PDF processing)

Setup
Get Free Accounts

Create a Neon.tech database

Get a Hugging Face token (free)

Install
Create requirements.txt:

txt
Copy
streamlit
langchain
psycopg2-binary
pypdf
python-dotenv
Run:

bash
Copy
pip install -r requirements.txt
Add Secrets
Create .env file:

env
Copy
HF_TOKEN=your_hf_token
NEON_DB_URL=postgres://user:password@neon-host/dbname?sslmode=require
Run

bash
Copy
streamlit run app.py
Design Choices
Free Database: Neon.tech for zero-cost PostgreSQL

Simple Chunks: 500-character text splits for basic context

Lightweight AI: Small embedding model to save resources

How It Works

Upload PDF → 2. Split text → 3. Save to database → 4. Ask questions → 5. Get answers

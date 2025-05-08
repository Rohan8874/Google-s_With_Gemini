# AI Legal Assistant with RAG

A Retrieval-Augmented Generation (RAG) system for legal document analysis, powered by Google Gemini and Streamlit.

## Features
- PDF document ingestion and processing
- Natural language query interface
- Context-aware legal responses
- Conversation history tracking
- FAISS-based vector search

## Prerequisites
- Python 3.9+
- Google API key (set in `.env`)
- RAM: Minimum 4GB (8GB recommended)

## Installation
1. Clone repository:
``bash
https://github.com/Rohan8874/Google-s_With_Gemini.git

## Install dependencies:

```bash
pip install -r requirements.txt
```
## Create .env file:
```env
GOOGLE_API_KEY=your_api_key_here
```
# Usage
1. Place PDF documents in pdfs/ directory

2. Generate vector database:

```bash
python vector_database.py
```
3. Launch web interface:

```bash
streamlit run frontend.py
```

## Project Structure

```

├── frontend.py            # Streamlit UI

├── rag_pipeline.py        # RAG processing

├── vector_database.py     # Vector DB management

├── requirements.txt       # Dependencies

└── pdfs/                  # Document storage

```
## Configuration

| Parameter           | Description                  | Default Value          |
|---------------------|------------------------------|------------------------|
| `chunk_size`        | Document splitting size      | 1000 characters        |
| `chunk_overlap`     | Overlap between chunks       | 200 characters         |
| `embedding_model`   | Google embedding model       | `models/embedding-001` |
| `llm_model`         | Google Generative AI model   | `gemini-2.0-flash`     |
# Troubleshooting
## Q: Getting "Missing PDF" error?

Ensure file is in pdfs/ directory

Verify PDF is not password protected

## Q: API key not working?

Check .env file formatting

Verify Google API permissions

## Q: Slow responses?

Reduce chunk size in vector_database.py

Use smaller PDF documents

## Known Limitations
Supports single PDF processing

# AI Fraud Detection Service

## Features
- Fraud risk analysis using Groq LLM
- RAG pipeline with ChromaDB
- Chunking (500 chars, 50 overlap)
- Structured JSON responses
- Report generation endpoint

## Endpoints

### /describe
POST → Fraud analysis

### /recommend
POST → Action recommendations

### /generate-report
POST → Detailed fraud report

### /health
GET → Service health check

## Tech Stack
- Flask
- ChromaDB
- Sentence Transformers
- Groq API

## Run
pip install -r requirements.txt
python app.py
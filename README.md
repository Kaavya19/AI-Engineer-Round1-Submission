# AI-Powered Communication Assistant

## Overview
An AI-powered system that fetches, filters, prioritizes, and responds to customer support emails while providing analytics on a dashboard.

## Features
- Email Retrieval (IMAP/Gmail/Outlook)
- NLP-based Categorization (Sentiment + Priority)
- Auto Response Generation (LLM + RAG)
- Dashboard with Analytics (emails processed, pending, sentiment breakdown)
- Key Info Extraction (contacts, requests, urgency)

## Tech Stack
- Backend: Python (Flask/FastAPI)
- NLP: Hugging Face / OpenAI GPT models
- Database: SQLite / PostgreSQL
- Frontend: React.js / Next.js
- Visualization: Chart.js / Recharts

## Setup Instructions
1. Clone repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` → `.env` and fill credentials.
3. Run backend:
   ```bash
   python backend/app.py
   ```
4. Run frontend:
   ```bash
   cd frontend && npm install && npm run dev
   ```

## Deliverables
- Working prototype
- Dashboard with analytics
- Documentation and slides
    

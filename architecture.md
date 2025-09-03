# System Architecture

## Flow
1. Email Fetcher → retrieves emails via IMAP/Gmail API
2. NLP Pipeline → extract sentiment, priority, key info
3. Priority Queue → urgent emails go first
4. Response Generator (LLM + RAG) → drafts professional replies
5. Dashboard → displays emails, analytics, and AI replies

## Diagram
[Email APIs] → [Backend/NLP] → [DB] → [Frontend Dashboard]
    
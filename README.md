# Dev Sentiment Agent

An AI-powered agent that scrapes dev forums like Reddit, analyzes community sentiment, and answers natural language queries about trending tech discussions.

## Features
- Reddit scraping via Bright Data (mocked in demo)
- Sentiment analysis using HuggingFace transformers
- LLM-based Q&A with LangChain + OpenAI
- Streamlit UI for prompt interaction

## Run Backend
```bash
cd backend
uvicorn main:app --reload
```

## Run Frontend
```bash
cd frontend
streamlit run app.py
```

## Example
"What is the mood on LangChain this week?"


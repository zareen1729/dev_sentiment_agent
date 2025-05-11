# Dev Sentiment Agent

An AI-powered agent that scrapes dev forums like Reddit, analyzes community sentiment, and answers natural language queries about trending tech discussions.

## Features
- Reddit scraping via Bright Data (mocked in demo)
- Sentiment analysis using HuggingFace transformers
- LLM-based Q&A with LangChain + OpenAI
- Streamlit UI for prompt interaction

## Setup Instructions

### Prerequisites
- Docker + Docker Compose
- OpenAI API Key

### Run the Project

```bash
git clone https://github.com/yourusername/dev_sentiment_agent.git
cd dev_sentiment_agent
docker-compose up --build
```

### Access the UI
Visit [http://localhost:8501](http://localhost:8501)

### Example Prompts
- "What's the mood on LangChain this week?"
- "Which vector database is most discussed lately?"

### Notes
- Replace mock data with Bright Data API integration in `scraper.py`.
- Add error handling and logging for production readiness.

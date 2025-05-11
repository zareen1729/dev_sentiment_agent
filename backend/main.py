from fastapi import FastAPI
from scraper import get_reddit_posts
from sentiment import analyze_sentiment
from langchain_agent import answer_query

app = FastAPI()

@app.get("/analyze")
def analyze(keyword: str):
    posts = get_reddit_posts(keyword)
    results = analyze_sentiment(posts)
    return {"results": results}

@app.get("/qa")
def qa(keyword: str, question: str):
    posts = get_reddit_posts(keyword)
    sentiments = analyze_sentiment(posts)
    answer = answer_query(sentiments, question)
    return {"answer": answer}

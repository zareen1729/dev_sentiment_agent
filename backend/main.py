from fastapi import FastAPI
from scraper import get_reddit_posts
from sentiment import analyze_sentiment

app = FastAPI()

@app.get("/analyze")
def analyze(keyword: str):
    posts = get_reddit_posts(keyword)
    results = analyze_sentiment(posts)
    return {"results": results}

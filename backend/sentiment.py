from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(posts):
    results = []
    for post in posts:
        content = post['title'] + "\n" + post.get('body', '')
        score = sentiment_analyzer(content[:512])[0]
        results.append({
            "title": post["title"],
            "sentiment": score["label"],
            "confidence": score["score"]
        })
    return results

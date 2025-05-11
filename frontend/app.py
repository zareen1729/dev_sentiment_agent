import streamlit as st
import requests

st.title("Dev Community Sentiment Agent")

query = st.text_input("Search tech topic (e.g., LangChain, AWS)")

if st.button("Analyze") and query:
    response = requests.get("http://localhost:8000/analyze", params={"keyword": query})
    results = response.json()["results"]
    for item in results:
        st.markdown(f"**{item['title']}**")
        st.write(f"Sentiment: {item['sentiment']} ({item['confidence']:.2f})")

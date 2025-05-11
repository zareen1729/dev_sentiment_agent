import streamlit as st
import requests

st.title("Dev Community Sentiment Agent")

query = st.text_input("Search tech topic (e.g., LangChain, AWS)")
prompt = st.text_input("Ask a question (e.g., What's trending in LLMs?)")

if st.button("Analyze") and query:
    response = requests.get("http://backend:8000/analyze", params={"keyword": query})
    results = response.json()["results"]
    for item in results:
        st.markdown(f"**{item['title']}**")
        st.write(f"Sentiment: {item['sentiment']} ({item['confidence']:.2f})")

if st.button("Ask") and query and prompt:
    response = requests.get("http://backend:8000/qa", params={"keyword": query, "question": prompt})
    st.subheader("Answer")
    st.write(response.json().get("answer", "No answer available"))

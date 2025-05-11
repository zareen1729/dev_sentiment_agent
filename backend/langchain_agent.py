from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

llm = OpenAI(temperature=0)
chain = load_qa_chain(llm, chain_type="stuff")

def answer_query(data, query):
    docs = [Document(page_content=entry["title"] + "\n" + entry.get("sentiment", "")) for entry in data]
    return chain.run(input_documents=docs, question=query)

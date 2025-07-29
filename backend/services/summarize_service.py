# backend/services/summarize_service.py

from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# T5 model: google/flan-t5-base
summarizer = pipeline("summarization", model="google/flan-t5-base", tokenizer="google/flan-t5-base", device=0)

llm = HuggingFacePipeline(pipeline=summarizer)

def summarize_text(text: str) -> str:
    # 1. chunk 분할
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])

    # 2. LangChain 체인 구성
    chain = load_summarize_chain(llm, chain_type="map_reduce")

    # 3. execute
    summary = chain.run(docs)
    return summary

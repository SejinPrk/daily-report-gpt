# backend/services/summarize_service.py

from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

summarizer = None
llm = None

def load_model():
    global summarizer, llm
    if summarizer is None:
        print("[INFO] Loading model to GPU...")
        summarizer = pipeline(
            "summarization",
            model="google/flan-t5-base",
            tokenizer="google/flan-t5-base",
            device=0  # CUDA:0
        )
        llm = HuggingFacePipeline(pipeline=summarizer)
        print("[INFO] Model loaded.")

# Main function
def summarize_text(text: str) -> str:
    load_model()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])

    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)

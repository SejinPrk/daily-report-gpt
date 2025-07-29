from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch
from typing import List, Dict

device = 0 if torch.cuda.is_available() else -1
print(f"[INFO] HuggingFace pipeline using device: {'cuda:0' if device == 0 else 'cpu'}")

model_name = "digit82/kobart-summarization"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_safetensors=True)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=device)

def generate_tags(summary: str) -> List[str]:
    keywords = summary.split()
    tags = [f"#{word.strip(',.')}" for word in keywords[:3]]
    return tags

def summarize_text(text: str) -> Dict[str, str]:
    try:
        print(f"[INFO] Summarizing text: {text}")
        result = summarizer(text, max_length=60, min_length=15, do_sample=False)
        summary = result[0]['summary_text'].strip()
        print(f"[DEBUG] summary = {summary}")

        tags = generate_tags(summary)
        print(f"[DEBUG] tags = {tags}")

        return {
            "summary": summary,
            "tags": tags,
            "feedback": "한글 특화 모델로 요약되었습니다."
        }

    except Exception as e:
        print(f"[ERROR] summarization failed: {e}")
        return {
            "summary": "",
            "tags": [],
            "feedback": "요약 중 오류가 발생했습니다."
        }

# backend/services/summarize_service.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch
from typing import List, Dict
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

device = 0 if torch.cuda.is_available() else -1
print(f"[INFO] HuggingFace pipeline using device: {'cuda:0' if device == 0 else 'cpu'}")

# 전역 초기화
model_name = "digit82/kobart-summarization"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_safetensors=True)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=device)
kw_model = KeyBERT(model=SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")) # 한글 지원 다국어 모델

def generate_tags(summary: str) -> List[str]:
    """
    요약 텍스트로부터 주요 키워드 해시태그 생성 (KeyBERT 사용)
    """
    try:
        keywords = kw_model.extract_keywords(
            summary,
            keyphrase_ngram_range=(1, 2),   # 단어 또는 2단어 키워드
            stop_words='korean',            # 불용어 제거
            top_n=5                         # Max: 5
        )

        if not keywords:
            print("[WARN] KeyBERT가 키워드를 추출하지 못했습니다. fallback 방식 사용")
            fallback_tags = [f"#{word.strip(',.')}" for word in summary.split()[:3]]
            return fallback_tags

        tags = [f"#{kw[0].replace(' ', '')}" for kw in keywords]  # 공백 제거 후 해시태그화
        print(f"[DEBUG] KeyBERT 추출 키워드: {tags}")
        return tags

    except Exception as e:
        print(f"[ERROR] generate_tags 실패: {e}")
        return []

def summarize_text(text: str) -> Dict[str, str]:
    """
    텍스트 요약 및 태그 추출
    """
    try:
        print(f"[INFO] Summarizing text: {text}")
        result = summarizer(
            text,
            max_new_tokens=200,             # 출력 길이 제한 (60 제거)
            do_sample=False,                # deterministic decoding
            num_beams=4,                    # Beam Search
            repetition_penalty=2.0,         # 중복 방지
            no_repeat_ngram_size=3          # n-gram 반복 방지
        )
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

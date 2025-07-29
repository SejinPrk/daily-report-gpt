# backend/services/tag_extractor.py

from typing import List
import re
from collections import Counter

def extract_tags(summary: str, top_n: int = 3) -> List[str]:
    # Optional: remove '요약:' prefix if present
    if summary.startswith("요약:"):
        summary = summary.replace("요약:", "").strip()

    # Extract candidate words (2+ characters, Korean or alphabetic)
    words = re.findall(r'\b[가-힣a-zA-Z]{2,}\b', summary)

    # Stopwords list (extend as needed)
    stopwords = {
        "입니다", "있습니다", "요약", "내용", "정리", "오늘", "업무", "입력된", "기반으로",
        "초기", "버전", "생성되었습니다", "정리했습니다", "수행했습니다", "진행했습니다"
    }

    # Filter words and count frequency
    keywords = [w for w in words if w not in stopwords and len(w) >= 2]
    common = Counter(keywords).most_common(top_n)

    # Convert to hashtags
    return [f"#{word}" for word, _ in common]

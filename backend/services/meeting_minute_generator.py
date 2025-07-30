# backend/services/meeting_minute_generator.py

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from typing import Dict
from backend.config import settings

llm = ChatOpenAI(
    temperature=settings.OPENAI_TEMPERATURE,
    model_name=settings.OPENAI_MODEL,
    openai_api_key=settings.OPENAI_API_KEY
)

prompt_template = PromptTemplate(
    input_variables=["date", "author", "participants", "location", "time_range", "raw_text"],
    template="""
다음은 {date}에 열린 회의에 대한 자유 형식 메모입니다.

작성자: {author}
참석자: {participants}
회의 장소: {location}
회의 시간: {time_range}

위 정보를 참고하여 아래 포맷으로 깔끔한 회의록을 작성하세요:

---
회의 목적:
논의 내용 요약:
결정 사항:
후속 액션 아이템:
---
회의록 내용은 자연스럽고 읽기 쉽게 요약해주세요.

원문:
{raw_text}
""",
)

meeting_chain = LLMChain(llm=llm, prompt=prompt_template)

def generate_meeting_minutes(meta: Dict[str, str]) -> str:
    """
    LangChain을 통해 회의록 정리

    Args:
        meta: {
            "date": "2025-07-30",
            "author": "Sejin",
            "participants": "Sejin, CTO, 백엔드 개발자",
            "location": "본사 / 회의실 A",
            "time_range": "09:30 ~ 10:30",
            "raw_text": "자유 형식 메모 원문"
        }

    Returns:
        회의록 정리된 문자열
    """
    return meeting_chain.run(meta)


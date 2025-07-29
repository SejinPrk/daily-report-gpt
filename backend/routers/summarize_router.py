# backend/routers/summarize_router.py

from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List

from backend.services.summarize_service import summarize_text

router = APIRouter()

# Request data model
class SummarizeRequest(BaseModel):
    text: str

# Response data model
class SummarizeResponse(BaseModel):
    summary: str
    tags: List[str]
    feedback: str

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_text_api(request: SummarizeRequest):
    summary = summarize_text(request.text)

    # todo: 태그, 피드백은 나중에 별도 추론 or 규칙 기반으로 확장
    return SummarizeResponse(
        summary=summary,
        tags=["#done"],
        feedback="초기 버전으로 요약이 생성되었습니다."
    )

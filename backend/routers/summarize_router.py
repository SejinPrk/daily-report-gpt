# backend/routers/summarize_router.py

from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List

router = APIRouter()

# 요청 데이터 모델
class SummarizeRequest(BaseModel):
    text: str

# 응답 데이터 모델
class SummarizeResponse(BaseModel):
    summary: str
    tags: List[str]
    feedback: str

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_text(request: SummarizeRequest):
    input_text = request.text

    # TODO: 이후 LangChain 요약 로직으로 교체할 예정
    dummy_summary = "요약: 입력된 업무 내용을 기반으로 핵심 내용을 정리했습니다."
    dummy_tags = ["#회의", "#보고서", "#리서치"]
    dummy_feedback = "업무 내용이 명확하게 정리되어 있어 좋습니다."

    return SummarizeResponse(
        summary=dummy_summary,
        tags=dummy_tags,
        feedback=dummy_feedback
    )

# backend/routers/summarize_router.py

from fastapi import APIRouter
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

@router.post("/tags", response_model=SummarizeResponse)
async def summarize_text_api(request: SummarizeRequest):
    summary_result = summarize_text(request.text) # dict

    return SummarizeResponse(
        summary=summary_result["summary"],   # str
        tags=summary_result["tags"], # str
        feedback=summary_result["feedback"]  # str
    )

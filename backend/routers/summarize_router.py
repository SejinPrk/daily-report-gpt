# backend/routers/summarize_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from backend.services.summarize_service import summarize_text
from backend.services.tag_extractor import extract_tags

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
    summary_result = summarize_text(request.text) # dict
    tags = extract_tags(summary_result["summary"])

    print("[DEBUG] summary =", summary_result)
    print("[DEBUG] tags =", tags)

    return SummarizeResponse(
        summary=summary_result["summary"],   # str
        tags=tags,                           # List[str]
        feedback=summary_result["feedback"]  # str
    )

# backend/routers/minute_router.py

from fastapi import APIRouter, Request
from pydantic import BaseModel
from backend.services.meeting_minute_generator import generate_meeting_minutes

router = APIRouter()

class MeetingMinuteRequest(BaseModel):
    content: str
    participants: list[str]

@router.post("/api/minutes", tags=["minutes"])
async def create_meeting_minutes(request: MeetingMinuteRequest, req: Request):
    try:
        # LangChain 기반 정리 function call
        # Todo: 임시로 필요한 필드값 구성 (나중에 프론트에서 받도록 확장 가능)
        meta = {
            "date": "2025-08-30",
            "author": "Sejin",
            "participants": ", ".join(request.participants),
            "location": "Corporate / Meeting Room A",
            "time_range": "09:30 ~ 10:30",
            "raw_text": request.content
        }

        minutes = generate_meeting_minutes(meta)

        return {
            "result": True,
            "status_code": "success",
            "minutes": minutes
        }
    except Exception as e:
        return {
            "result": False,
            "status_code": "error",
            "description": str(e)
        }

# backend/routers/minute_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.meeting_minute_generator import generate_meeting_minutes

router = APIRouter()

class MeetingMinuteRequest(BaseModel):
    date: str
    author: str
    participants: str
    location: str
    time_range: str
    raw_text: str

@router.post("/minutes", tags=["minutes"])
async def create_meeting_minutes(request: MeetingMinuteRequest):
    try:
        # LangChain 기반 정리 function call
        minutes = generate_meeting_minutes(request.model_dump())

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

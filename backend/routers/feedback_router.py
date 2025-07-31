# backend/routers/feedback_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.feedback_generator import generate_feedback

router = APIRouter()

class FeedbackRequest(BaseModel):
    meeting_minutes: str

@router.post("/feedback", tags=["feedback"])
async def create_feedback(request: FeedbackRequest):
    try:
        feedback = generate_feedback(request.meeting_minutes)

        return {
            "result": True,
            "status_code": "success",
            "feedback": feedback
        }
    except Exception as e:
        return {
            "result": False,
            "status_code": "error",
            "description": str(e)
        }

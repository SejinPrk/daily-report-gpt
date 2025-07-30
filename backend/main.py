# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import summarize_router, minute_router

app = FastAPI(
    title="DailyReportGPT API",
    description="AI-powered daily report summarizer and tag extractor",
    version="0.1.0"
)

# CORS setting
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vue 프론트와 통신하려면 "*" 또는 "http://localhost:5173"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router setting
app.include_router(summarize_router.router, prefix="/api") # summarize router
app.include_router(minute_router.router) # minute router

@app.get("/")
async def root():
    return {"message": "Hello from Daily Report GPT!"}
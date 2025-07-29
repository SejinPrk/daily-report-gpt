# DailyReportGPT 📋  
An AI-powered tool that summarizes intern logs, extracts tags, and generates weekly reports.  
**AI 기반 회의록/업무일지 요약 및 태그 생성기 프로젝트입니다.**

---

## Overview | 개요
This project allows users to upload meeting notes or daily reports. The system uses LLMs to:
- Summarize content (daily or weekly)
- Extract key task-related tags
- Provide brief feedback or insights

사용자가 회의록 또는 일일 업무일지를 업로드하면 시스템은 다음을 자동으로 수행합니다:
- 일일/주간 요약 생성  
- 주요 태스크 기반 태그 추출  
- 간단한 피드백 생성

---

## Tech Stack | 기술 스택
**Backend**
- Python 3.10, FastAPI, LangChain, Milvus  
**Frontend**
- Vue 3, Pinia, TailwindCSS  
**Embedding Models**
- BGE-M3, BGE Reranker

---

## eatures | 주요 기능
- Upload text-based logs or reports | 텍스트 기반 업무일지 업로드
- Summarize daily/weekly logs | 일일/주간 업무 요약 자동 생성
- Extract hashtags (e.g., `#meeting`, `#reporting`, `#research`) | 업무 키워드 자동 태그화
- Export to Notion or Excel (TODO) | 노션 또는 Excel로 변환 저장 (TODO)

---

## 🚀 Getting Started | 실행 방법

```bash
# Backend
cd backend
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

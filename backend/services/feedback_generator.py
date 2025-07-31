# backend/services/feedback_generator.py

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from backend.config import settings

llm = ChatOpenAI(
    temperature=0.4,
    model_name=settings.OPENAI_MODEL,
    openai_api_key=settings.OPENAI_API_KEY
)

feedback_prompt = PromptTemplate(
    input_variables=["meeting_minutes"],
    template="""
            다음은 회의 요약본입니다.  
            이 회의의 내용과 흐름을 바탕으로 회의 방식에 대한 피드백을 한 줄로 작성해주세요.  
            좋은 점 또는 개선할 점을 언급해주세요.  
            회의 내용이 체계적으로 진행되었는지, 불필요한 내용으로 지연되었는지, 결정 사항이 명확했는지 등을 평가해 주세요.

            회의 요약:  
            {meeting_minutes}

            피드백:
    """
)

feedback_chain = LLMChain(llm=llm, prompt=feedback_prompt)

def generate_feedback(meeting_minutes: str) -> str:
    """
    회의 내용 기반 피드백 생성

    Args:
        meeting_minutes: 요약된 회의록 문자열

    Returns:
        피드백 한 줄 문자열
    """
    return feedback_chain.run({"meeting_minutes": meeting_minutes})

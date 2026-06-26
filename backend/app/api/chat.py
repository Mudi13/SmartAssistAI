from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.ai.services.ai_service import chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    
@router.post("/chat")
def chat_api(data: ChatRequest):
    answer = chat(data.message)
    
    return {
        "response" : answer
    }
    
    
from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_service import chat_service
from app.prompts.prompt_manager import prompt_manager

router = APIRouter()


@router.get("/welcome", summary="Get the chatbot welcome message")
def get_welcome():
    return {"welcome_message": prompt_manager.get_welcome_message()}


@router.post("/", response_model=ChatResponse, summary="Send a message to the chatbot")
async def chat(request: ChatRequest):
    reply = await chat_service.get_response(
        user_message=request.user_message,
        chat_history=request.chat_history,
    )
    return ChatResponse(reply=reply)
from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import generate_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    reply = generate_response(
        user_id=request.user_id,
        user_input=request.message
    )

    return ChatResponse(reply=reply)
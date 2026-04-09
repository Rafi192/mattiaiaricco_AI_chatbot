from fastapi import APIRouter, Form
# from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import generate_response
from fastapi import Query
from app.services.history_service import get_chat_history

router = APIRouter()

@router.post("/api/chat/")
def chat(
    user_id: str = Form(),
    query: str = Form()
):
    reply = generate_response(
        user_id=user_id,
        user_input=query
    )

    return {"reply": reply}



@router.get("/api/chat/history/")
def get_history(
    user_id: str = Query(...), # get requests should use query parameters, not form data
    limit: int = Query(10)
):
    history = get_chat_history(user_id, limit)

    return {
        "user_id": user_id,
        "messages": history
    }

# @router.post("/chat", response_model=ChatResponse)
# def chat_endpoint(request: ChatRequest):
#     reply = generate_response(
#         user_id=request.user_id,
#         user_input=request.message
#     )

#     return ChatResponse(reply=reply)
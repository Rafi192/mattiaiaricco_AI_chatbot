from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat, admin

app = FastAPI(
    title="Emergency Response Chatbot API",
    description="AI-powered chatbot for emergency guidance (fire, earthquake, first aid, etc.)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "Emergency Chatbot API is running."}
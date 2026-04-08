from fastapi import FastAPI
from app.api import chat, admin

app = FastAPI(title="Emergency AI Chatbot")

app.include_router(chat.router)
app.include_router(admin.router)
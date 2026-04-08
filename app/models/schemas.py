from pydantic import BaseModel, Field
from typing import List, Optional


# ── Chat schemas ────────────────────────────────────────────────────────────

class MessageHistory(BaseModel):
    role: str = Field(..., description="'human' or 'assistant'")
    content: str


class ChatRequest(BaseModel):
    user_message: str = Field(..., min_length=1, description="The user's message")
    chat_history: Optional[List[MessageHistory]] = Field(
        default=[],
        description="Previous turns in the conversation for multi-turn memory",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "user_message": "There is a fire in my kitchen, what should I do?",
                "chat_history": [],
            }
        }


class ChatResponse(BaseModel):
    reply: str
    detected_language: Optional[str] = None


# ── Admin schemas ───────────────────────────────────────────────────────────

class UpdateWelcomeMessage(BaseModel):
    welcome_message: str = Field(..., min_length=1)


class UpdateSystemInstruction(BaseModel):
    system_instruction: str = Field(..., min_length=1)


class UpdateFallbackResponse(BaseModel):
    fallback_response: str = Field(..., min_length=1)


class PromptConfig(BaseModel):
    welcome_message: str
    system_instruction: str
    fallback_response: str
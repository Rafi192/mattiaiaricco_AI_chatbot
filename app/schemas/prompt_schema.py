from pydantic import BaseModel
from typing import Optional


class PromptUpdateRequest(BaseModel):
    welcome_instruction: Optional[str] = None
    system_instruction: Optional[str] = None
    fallback_message: Optional[str] = None
from app.prompts.defaults import (
    DEFAULT_WELCOME_MESSAGE,
    DEFAULT_SYSTEM_INSTRUCTION,
    DEFAULT_FALLBACK_RESPONSE,
)
 
 
class PromptManager:
    def __init__(self):
        self._welcome_message: str = DEFAULT_WELCOME_MESSAGE
        self._system_instruction: str = DEFAULT_SYSTEM_INSTRUCTION
        self._fallback_response: str = DEFAULT_FALLBACK_RESPONSE
 
    # ── Getters ────────────────────────────────────────────────────────────
    def get_welcome_message(self) -> str:
        return self._welcome_message
 
    def get_system_instruction(self) -> str:
        return self._system_instruction
 
    def get_fallback_response(self) -> str:
        return self._fallback_response
 
    # ── Setters (called by admin API) ──────────────────────────────────────
    def update_welcome_message(self, message: str) -> None:
        self._welcome_message = message
 
    def update_system_instruction(self, instruction: str) -> None:
        self._system_instruction = instruction
 
    def update_fallback_response(self, response: str) -> None:
        self._fallback_response = response
 
    def get_all(self) -> dict:
        return {
            "welcome_message": self._welcome_message,
            "system_instruction": self._system_instruction,
            "fallback_response": self._fallback_response,
        }
 
 
# Singleton — shared across the whole application
prompt_manager = PromptManager()
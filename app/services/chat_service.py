
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
 
from app.config import settings
from app.prompts.prompt_manager import prompt_manager
from app.prompts.template import build_chat_prompt
from app.models.schemas import MessageHistory
 
 
class ChatService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.openai_model,
            temperature=settings.openai_temperature,
            max_tokens=settings.openai_max_tokens,
            openai_api_key=settings.openai_api_key,
        )
 
    def _convert_history(self, history: list[MessageHistory]):
        """Convert flat history dicts to LangChain message objects."""
        messages = []
        for msg in history:
            if msg.role == "human":
                messages.append(HumanMessage(content=msg.content))
            elif msg.role == "assistant":
                messages.append(AIMessage(content=msg.content))
        return messages
 
    async def get_response(
        self, user_message: str, chat_history: list[MessageHistory]
    ) -> str:
        system_instruction = prompt_manager.get_system_instruction()
        fallback = prompt_manager.get_fallback_response()
 
        prompt = build_chat_prompt(system_instruction)
        chain = prompt | self.llm | StrOutputParser()
 
        lc_history = self._convert_history(chat_history)
 
        try:
            response = await chain.ainvoke(
                {
                    "user_message": user_message,
                    "chat_history": lc_history,
                }
            )
            return response.strip() if response.strip() else fallback
        except Exception as exc:
            # Log in production; return a safe fallback to the user
            print(f"[ChatService] Error calling OpenAI: {exc}")
            return fallback
 
 
# Singleton
chat_service = ChatService()
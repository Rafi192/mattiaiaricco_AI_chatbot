from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def build_chat_prompt(system_instruction: str) -> ChatPromptTemplate:
    """
    Builds a LangChain ChatPromptTemplate with:
      - A dynamic system instruction (set by admin)
      - The full conversation history (multi-turn memory)
      - The latest human message
    """
    return ChatPromptTemplate.from_messages(
        [
            ("system", system_instruction),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{user_message}"),
        ]
    )
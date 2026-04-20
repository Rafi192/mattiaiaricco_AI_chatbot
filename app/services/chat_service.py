from openai import OpenAI
from app.core.config import settings
from app.core.prompts import chat_prompt
from app.services.history_service import save_message, get_chat_history
from app.services.admin_service import get_prompt_config
# import asyncio
# from functools import partial

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def format_history(history):
    formatted = []
    for msg in history:
        role = "human" if msg["role"] == "user" else "ai"
        formatted.append((role, msg["content"]))
    return formatted


ROLE_MAPPING = {
    "system": "system",
    "human": "user",
    "ai": "assistant"
}

def convert_prompt_to_openai_messages(prompt_messages):
   
    openai_messages = []
    for msg in prompt_messages:
        role = ROLE_MAPPING.get(msg.type)  
        if not role:
            continue 
        openai_messages.append({
            "role": role,
            "content": msg.content
        })
    return openai_messages

def _normalize_language(language: str) -> str:
    value = (language or "en").strip().lower().replace("_", "-")
    if value.startswith("it"):
        return "it"
    return "en"


def _language_instruction(language: str) -> str:
    code = _normalize_language(language)
    if code == "it":
        return (
            "Selected app language: Italian (it). Respond only in Italian, "
            "including steps, warnings, and emergency service reminders, unless "
            "the user explicitly asks for another language."
        )
    return (
        "Selected app language: English (en). Respond only in English, "
        "including steps, warnings, and emergency service reminders, unless "
        "the user explicitly asks for another language."
    )


def generate_response(
    user_id: str,
    user_input: str,
    emergency_type: str = "General Emergency",
    language: str = "en"
):
    config = get_prompt_config()

    history = get_chat_history(user_id)
    formatted_history = format_history(history)
    selected_emergency_type = emergency_type or "General Emergency"

    #  LangChain prompt from my core.prompts
    prompt = chat_prompt.invoke({
        "welcome_instruction": config.get("welcome_instruction"),
        "system_instruction": config.get("system_instruction"),
        "fallback_message": config.get("fallback_message"),
        "response_language_instruction": _language_instruction(language),
        "emergency_type": selected_emergency_type,
        "history": formatted_history,
        "user_input": user_input
    })

    messages = convert_prompt_to_openai_messages(prompt.to_messages())

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=messages
        # temperature=0.2
    )

    reply = response.choices[0].message.content

    # Save messages
    save_message(user_id, "user", user_input)
    save_message(user_id, "assistant", reply)

    return reply


# def generate_response(user_id: str, user_input: str):
#     config = get_prompt_config()

#     history = get_chat_history(user_id)

#     # Convert history to OpenAI roles
#     messages = []
#     # Add system instruction
#     if config.get("system_instruction"):
#         messages.append({"role": "system", "content": config["system_instruction"]})

#     # Add previous conversation
#     for msg in history:
#         role = "user" if msg["role"] == "user" else "assistant"
#         messages.append({"role": role, "content": msg["content"]})

#     # Add welcome message if this is the first user message
#     if not history and config.get("welcome_instruction"):
#         messages.append({"role": "system", "content": config["welcome_instruction"]})

#     # Add current user input
#     messages.append({"role": "user", "content": user_input})

#     # Call OpenAI
#     # loop = asyncio.get_event_loop()
#     response = client.chat.completions.create(
#         model="gpt-5-mini",
#         messages=messages
#         # temperature = 1
#     )
#     # response = await loop.run_in_executor(
#     #     None,
#     #     partial(client.chat.completions.create, model="gpt-5-mini", messages=messages)
#     # )

#     reply = response.choices[0].message.content

#     # Save messages
#     save_message(user_id, "user", user_input)
#     save_message(user_id, "assistant", reply)

#     return reply






#-----------------------------------------------------------------

# def generate_response(user_id: str, user_input: str):
#     config = get_prompt_config()

#     history = get_chat_history(user_id)
#     formatted_history = format_history(history)

#     prompt = chat_prompt.invoke({
#         "welcome_instruction": config.get("welcome_instruction"),
#         "system_instruction": config.get("system_instruction"),
#         "fallback_message": config.get("fallback_message"),
#         "history": formatted_history,
#         "user_input": user_input
#     })

#     response = client.chat.completions.create(
#         model="gpt-5-mini",
#         messages=prompt.to_messages(),
#         temperature=0.2
#     )

#     reply = response.choices[0].message.content

#     save_message(user_id, "user", user_input)
#     save_message(user_id, "assistant", reply)

#     return reply


from openai import OpenAI
from app.core.config import settings
from app.core.prompts import chat_prompt
from app.services.history_service import save_message, get_chat_history
from app.services.admin_service import get_prompt_config

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def format_history(history):
    formatted = []
    for msg in history:
        role = "human" if msg["role"] == "user" else "ai"
        formatted.append((role, msg["content"]))
    return formatted


def generate_response(user_id: str, user_input: str):
    config = get_prompt_config()

    history = get_chat_history(user_id)
    formatted_history = format_history(history)

    #  LangChain prompt from my core.prompts
    prompt = chat_prompt.invoke({
        "welcome_instruction": config.get("welcome_instruction"),
        "system_instruction": config.get("system_instruction"),
        "fallback_message": config.get("fallback_message"),
        "history": formatted_history,
        "user_input": user_input
    })

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=prompt.to_messages(),
        temperature=0.2
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
#     response = client.chat.completions.create(
#         model="gpt-5-mini",
#         messages=messages
#         # temperature = 1
#     )

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


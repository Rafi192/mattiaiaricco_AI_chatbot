from datetime import datetime
from app.db.mongo import prompt_collection
from app.core.prompts import chat_prompt, DEFAULT_WELCOME_MESSAGE, DEFAULT_SYSTEM_INSTRUCTION, DEFAULT_FALLBACK_RESPONSE

def get_prompt_config():
    config = prompt_collection.find_one({"type": "global_prompt"})

    if not config:
        return {
            "welcome_instruction": DEFAULT_WELCOME_MESSAGE,
            "system_instruction": DEFAULT_SYSTEM_INSTRUCTION,
            "fallback_message": DEFAULT_FALLBACK_RESPONSE
        }
    
    # if any field is missing, then the mongoBD collection will return None, so we need to provide default values
    return {
        "welcome_instruction": config.get("welcome_instruction") or DEFAULT_WELCOME_MESSAGE,
        "system_instruction": config.get("system_instruction") or DEFAULT_SYSTEM_INSTRUCTION,
        "fallback_message": config.get("fallback_message") or DEFAULT_FALLBACK_RESPONSE
    }


def update_prompt_config(update_data: dict):
    update_data["updated_at"] = datetime.utcnow()

    prompt_collection.update_one(
        {"type": "global_prompt"},
        {"$set": update_data},
        upsert=True
    )
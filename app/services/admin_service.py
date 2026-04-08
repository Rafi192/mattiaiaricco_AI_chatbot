from datetime import datetime
from app.db.mongo import prompt_collection


def get_prompt_config():
    config = prompt_collection.find_one({"type": "global_prompt"})

    if not config:
        return {
            "welcome_instruction": "Greet the user politely and ask how you can help.",
            "system_instruction": "Provide emergency guidance.",
            "fallback_message": "Please contact emergency services."
        }

    return config


def update_prompt_config(update_data: dict):
    update_data["updated_at"] = datetime.utcnow()

    prompt_collection.update_one(
        {"type": "global_prompt"},
        {"$set": update_data},
        upsert=True
    )
from datetime import datetime
from app.db.mongo import chat_collection

def save_message(user_id:str, role:str, content:str):
    chat_collection.update_one(
        {"user_id": user_id},
        {"$push":{
            "messages": {
                "role":role,
                "content": content,
                "timestamp": datetime.now()
            }
        }},
        upsert=True
    )

def get_chat_history(user_id:str, limit: int = 10):
    data = chat_collection.find_one({"user_id": user_id})
    if not data:
        return []
    return data.get("messages", [])[-limit:]
from pymongo import MongoClient
from app.core.config import settings
import os
client = MongoClient(settings.MONGO_URI)

# opeai_api = settings.OPENAI_API_KEY

db = client[os.getenv("MONGODB_DATABASE", "mattiaiarriccio")]

chat_collection = db[os.getenv("MONGODB_COLLECTION", "chat_history")]
prompt_collection = db[os.getenv("MONGODB_PROMPT_COLLECTION", "prompt_config")]

# print(f"Connected to MongoDB at {settings.MONGO_URI}, using database '{db.name}' and collection '{chat_collection.name}'")
# print(f"OpenAI API Key:", opeai_api)
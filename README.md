# Emergency Response Chatbot

An AI chatbot powered by OpenAI GPT and LangChain, specialized in step-by-step emergency guidance. Supports fire, earthquake, blackout, first aid, CPR, and more. Auto-detects and responds in the user's language (English, Italian, etc.).

## Project Structure

```
AI_chatbot/
├── main.py                    
├── .env                         
├── .env.example                  
├── requirements.txt
├── .gitignore
└── app/
    ├── config.py                  
    ├── routers/
    │   ├── chat.py                
    │   └── admin.py               
    ├── services/
    │   ├── chat_service.py        
    │   └── admin_service.py      
    ├── prompts/
    │   ├── defaults.py            
    │   ├── prompt_manager.py      
    │   └── templates.py          
    └── models/
        └── schemas.py             
```

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv chatbot_env
source chatbot_env/bin/activate      # Windows: chatbot_env\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure secrets
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 4. Run the server
uvicorn main:app --reload
```

API docs available at: http://localhost:8000/docs

## Key API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/chat/welcome` | Get current welcome message |
| POST | `/api/v1/chat/` | Send a message, get AI response |
| GET | `/api/v1/admin/config` | View all active prompts |
| PATCH | `/api/v1/admin/welcome-message` | Update welcome message |
| PATCH | `/api/v1/admin/system-instruction` | Update system instruction |
| PATCH | `/api/v1/admin/fallback-response` | Update fallback response |

## Multi-language Support

The system prompt instructs the model to detect and mirror the user's language automatically. No extra code needed — if a user writes in Italian, the bot responds in Italian.

## Notes

- The `PromptManager` stores prompt config in memory. For production, replace it with a database-backed store (PostgreSQL, Redis, etc.).
- Protect `/api/v1/admin/*` endpoints with authentication before deploying publicly.
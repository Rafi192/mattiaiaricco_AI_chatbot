from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key:str
    openai_model:str ="gpt-5-mini"
    openai_temp:float =0.2
    max_tokens:int = 1024

    class config:
        env_file = ".env"
        env_file

settings = Settings()
 
from fastapi import APIRouter, Form
from app.schemas.prompt_schema import PromptUpdateRequest
from app.services.admin_service import (
    update_prompt_config,
    get_prompt_config
)

router = APIRouter(prefix="/admin")


@router.get("/prompt")
def get_prompt():
    return get_prompt_config()


@router.patch("/prompt")
def update_prompt(
    welcome_message:str = Form("hello there"),
    system_instruction:str = Form("provide emergency guidance..."),
    fallback_message:str = Form("please contact emergency services...")
):
    # update_data = request.model_dump(exclude_unset=True)

    update_data = {}
    if welcome_message is not None:
        update_data["welcome_instruction"] = welcome_message
    
    if system_instruction is not None:
        update_data["system_instruction"] = system_instruction
    
    if fallback_message is not None:
        update_data["fallback_message"]= fallback_message
    

    if not update_data:
        return {"message": "No fields provided"}

    update_prompt_config(update_data)

    return {"message": "Prompt updated successfully"}
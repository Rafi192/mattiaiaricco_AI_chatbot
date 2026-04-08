from fastapi import APIRouter
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
def update_prompt(request: PromptUpdateRequest):
    update_data = request.model_dump(exclude_unset=True)

    if not update_data:
        return {"message": "No fields provided"}

    update_prompt_config(update_data)

    return {"message": "Prompt updated successfully"}
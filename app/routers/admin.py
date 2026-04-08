from fastapi import APIRouter
from app.models.schemas import (
    UpdateWelcomeMessage,
    UpdateSystemInstruction,
    UpdateFallbackResponse,
    PromptConfig,
)
from app.services.admin_service import admin_service
 
router = APIRouter()
 
 
@router.get("/config", response_model=PromptConfig, summary="Get current prompt config")
def get_config():
    return admin_service.get_current_config()
 
 
@router.patch("/welcome-message", summary="Update the welcome message")
def update_welcome(body: UpdateWelcomeMessage):
    admin_service.update_welcome_message(body.welcome_message)
    return {"detail": "Welcome message updated successfully."}
 
 
@router.patch("/system-instruction", summary="Update the system instruction")
def update_system(body: UpdateSystemInstruction):
    admin_service.update_system_instruction(body.system_instruction)
    return {"detail": "System instruction updated successfully."}
 
 
@router.patch("/fallback-response", summary="Update the fallback response")
def update_fallback(body: UpdateFallbackResponse):
    admin_service.update_fallback_response(body.fallback_response)
    return {"detail": "Fallback response updated successfully."}
 
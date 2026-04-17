from fastapi import APIRouter, Depends
from app.services.session_service import SessionService
from app.clients.ollama import generate_response

from app.schemas import SessionResult

router = APIRouter()
session_service = SessionService()


@router.get("/session_summary", response_model=SessionResult)
async def session_summary(
    service : SessionService = Depends(lambda: session_service),
    name : str = "Franco COLAPINTO",
):
    result = await service.get_latest_session_result(name=name)
    summary = await generate_response(
        driver_name=result["driver_name"],
        position=result["position"],
        points=result["points"]
    )
    return summary
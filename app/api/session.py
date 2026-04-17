from fastapi import APIRouter, Depends
from app.services.session_service import SessionService

from app.schemas import SessionResult

router = APIRouter()
session_service = SessionService()


@router.get("/session_summary")
async def session_summary(
    service : SessionService = Depends(lambda: session_service),
    name : str = "Max Verstappen",
):
    result = await service.get_latest_session_result(name=name)
    return result
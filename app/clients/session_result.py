from app.clients.base import fetch

async def get_session_result(params : dict = None) -> dict:
    return await fetch('/session_result', params=params)
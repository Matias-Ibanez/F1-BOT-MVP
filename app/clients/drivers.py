from app.clients.base import fetch

async def get_drivers(params : dict = None) -> dict:
    return await fetch('/drivers', params=params)
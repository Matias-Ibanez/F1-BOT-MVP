from app.clients.session_result import get_session_result

class SessionService:
    def __init__(self):
        pass

    async def get_latest_session_result(self) -> dict:
        # Here you would call the client to fetch the session result
        # For now, we'll return a dummy summary
        session_result = await get_session_result()
        return session_result
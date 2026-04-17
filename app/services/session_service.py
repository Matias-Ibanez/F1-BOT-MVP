from app.clients.session_result import get_session_result
from app.clients.drivers import get_drivers

class SessionService:
    def __init__(self):
        pass

    async def get_latest_session_result(self, name: str) -> dict:

            drivers = await get_drivers()

            driver = next(
                (d for d in drivers if name.lower() in d["full_name"].lower()),
                None
            )

            if not driver:
                raise ValueError(f"Driver '{name}' not found")

            driver_number = driver["driver_number"]

            session_result = await get_session_result(
                params={"driver_number": driver_number}
            )

            if not session_result:
                raise ValueError("No results found for this driver")

            session_result = session_result[0]  

            return {
                "position": session_result["position"],
                "driver_number": driver_number,
                "driver_name": driver["full_name"],
                "points": session_result.get("points", 0)
            }
            
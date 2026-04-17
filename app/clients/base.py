import httpx

BASE_URL = 'https://api.openf1.org/v1'

async def fetch(
    endpoint: str,
    params: dict  | None = None) -> dict: #type: ignore
    if not params: 
        params = {
            "meeting_key" : 1281,
            "session_key" : 11253,
        }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        print(f"Error fetching {endpoint}: {e}")
        raise
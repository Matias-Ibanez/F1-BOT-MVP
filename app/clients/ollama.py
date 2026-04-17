import httpx

async def generate_response(driver_name: str, position: int, points: int) -> str:
    prompt = f"""
You are a professional Formula 1 journalist.

Write a race report (2-3 sentences) about the driver's performance.

Driver: {driver_name}
Finishing Position: {position}
Points Earned: {points}

The tone should be engaging and similar to a sports news article.
Do not repeat the data mechanically—write it naturally. The response should be in spanish.
"""

    async with httpx.AsyncClient(base_url="http://ollama:11434", timeout=60.0) as client:
        response = await client.post(
            "/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            }
        )

    return response.json()["response"]
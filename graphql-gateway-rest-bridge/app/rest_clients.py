import httpx
from .settings import settings
async def fetch_json(path: str):
    async with httpx.AsyncClient(timeout=settings.timeout_seconds) as client:
        resp = await client.get(f"{settings.rest_base_url}{path}")
        resp.raise_for_status()
        return resp.json()
async def get_post(post_id: int): return await fetch_json(f"/posts/{post_id}")
async def list_posts(limit: int = 10):
    data = await fetch_json("/posts")
    return data[:limit]
async def get_user(user_id: int): return await fetch_json(f"/users/{user_id}")

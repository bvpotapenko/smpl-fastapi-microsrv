import pytest
import httpx
from app.main import app

@pytest.mark.asyncio
async def test_read_root_async():
    async with httpx.AsyncClient(app=app, base_url="http://test") as async_client:
        response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
import pytest

@pytest.mark.asyncio
async def test_read_root_async(async_client):
    # response = await async_client.get("/")
    response = async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
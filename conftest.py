import pytest
import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def async_client():
    client = TestClient(app)
    return client
# async def async_client():
#     async with httpx.AsyncClient(app=app, base_url="http://test") as client:
#         yield client
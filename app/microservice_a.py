# uvicorn microservice_a:app --reload --port 8001
import logging
from app.logging_config import setup_logging
from fastapi import FastAPI

# Configure logging
log_file_path = "logs/app.log"
setup_logging(log_file_path)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_a():
    logger.info("Handling request for Microservice A")
    return {"Microservice": "A"}
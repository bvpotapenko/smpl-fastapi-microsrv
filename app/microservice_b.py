# uvicorn microservice_b:app --reload --port 8002
import logging
from app.logging_config import setup_logging
from fastapi import FastAPI

# Configure logging
log_file_path = "logs/app.log"
setup_logging(log_file_path)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_b():
    logger.info("Handling request for Microservice B")
    return {"Microservice": "B"}
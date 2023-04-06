from app.logging_config import setup_logging
import logging
from fastapi import FastAPI

# Configure logging
log_file_path = "logs/app.log"
setup_logging(log_file_path)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Handling request for read_root main")
    return{"Hello": "World"}
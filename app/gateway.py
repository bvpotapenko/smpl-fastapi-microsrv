# uvicorn app.gateway:app --reload --port 8003
import httpx
import logging
from app.logging_config import setup_logging
from fastapi import FastAPI
import yaml

# Configure logging
log_file_path = "logs/app.log"
setup_logging(log_file_path)
logger = logging.getLogger(__name__)

# Read the configuration file
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# Access the configuration values
main_service_name = config["main_service_name"]
print(main_service_name)
a_service_name = config["a_service_name"]
b_service_name = config["b_service_name"]

log_file_path = "app.log"
setup_logging(log_file_path)

app = FastAPI()

async def fetch_microservice(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

@app.get("/")
async def read_gateway():
    logger.info("Handling request for read_gateway")
    response_main = await fetch_microservice(main_service_name)
    response_a = await fetch_microservice(a_service_name)
    response_b = await fetch_microservice(b_service_name)
    
    return {
        "Main": response_main,
        "Microservice A": response_a,
        "Microservice B": response_b
    }
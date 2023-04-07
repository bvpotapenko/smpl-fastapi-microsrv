# FastAPI Gateway Project

## Description
This project is a simple API Gateway built with FastAPI. The API Gateway is designed to route requests to various microservices and provide a single entry point for clients.

## Requirements
Python 3.9+
FastAPI
Uvicorn
HTTPX
Pytest

## Installation
1. Clone the project repository:
```bash
git clone https://github.com/your-username/fastapi-gateway.git
```

2. Navigate to the project directory:
```bash
cd fastapi-gateway
```

3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
1. Start the application using Uvicorn:
```bash
uvicorn main:app --reload --port 8000
uvicorn microservice_a:app --reload --port 8001
uvicorn microservice_b:app --reload --port 8002
uvicorn app.gateway:app --reload --port 8003
```
2. The gateway will be accessible at http://127.0.0.1:8003 

## Running Tests
1. Install the required test dependencies:
```bash
pip install -r requirements-test.txt
```

2. Run the tests using Pytest:
```bash
pytest tests/test_main_async.py
pytest tests/test_main_async2.py
pytest tests/test_main_sync.py
```

## Project Structure
```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── logging_config.py
│   └── services.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main_async.py
│   └── test_main_sync.py
├── .gitignore
├── README.md
├── requirements.txt
└── requirements-test.txt
```
## Usage
1. Update the config.py file with the necessary information about the microservices.
2. Make requests to the API Gateway using the appropriate endpoints, and the gateway will route the requests to the respective microservices.
3. Check the log file gateway.log for logs related to the API Gateway.

## Contributing
Feel free to submit issues, create pull requests or fork the project to make your own improvements. We appreciate any contributions!
=======

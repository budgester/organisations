# Organisations API

A FastAPI application that provides a REST API for managing organisations.

## Features

- GET `/organisations` - Returns a JSON list of organisations
- Interactive Swagger UI documentation at `/docs`
- ReDoc documentation at `/redoc`

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```

Access the API:
- API endpoint: http://127.0.0.1:8000/organisations
- Swagger UI: http://127.0.0.1:8000/docs

## Example Response

```json
[
  {
    "id": 1,
    "name": "Acme Corp",
    "description": "A technology company"
  },
  {
    "id": 2,
    "name": "Global Industries",
    "description": "Manufacturing and logistics"
  }
]
```

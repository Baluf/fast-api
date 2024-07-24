# Simple FastAPI Project
This is a simple project built with FastAPI to learn the basics of creating APIs. The project uses SQLite as the database and is intended for educational purposes.

## Features

- Basic CRUD operations
- SQLite database for local storage
- Simple FastAPI structure
- Requirements
- Python 3.7+
- FastAPI
- SQLAlchemy (or another ORM of choice)
- SQLite (built-in with Python)

## Installation 

- Clone the Repository

```bash
git clone https://github.com/yourusername/fast-api.git
cd fast-api
```

- Create virtual python env

```bash
python -m venv venv
source venv/bin/activate
```

- Install Dependencies

```bash
pip install -r requirements.txt
```

- Run the Application
  
```bash
uvicorn main:app --reload
```
This will start the FastAPI server on http://127.0.0.1:8000.

- Access the API Documentation
FastAPI provides automatic interactive API documentation:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

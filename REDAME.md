# Calculator API

A simple calculator API built with FastAPI.

## Features

- `GET /health` checks that the API is running.
- `POST /calculate` performs addition, subtraction, multiplication, and division.
- `GET /history` returns recent calculations.

## Run the project

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
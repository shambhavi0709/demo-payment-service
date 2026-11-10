# Demo Payment Service

A small FastAPI application used as the monitored repository for BuildSentry.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the API documentation.

## Run tests

```bash
pytest -v
```

## CI

GitHub Actions runs the test suite on pushes and pull requests targeting `main`.

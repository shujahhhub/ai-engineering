# AI Engineering Roadmap

Python learning exercises for the first five days of the AI engineering
roadmap.

## Repository structure

```text
.
└── week-01-python-fastapi/
    ├── day-01-python-basics/
    ├── day-02-python/
    ├── day-03-python/
    ├── day-04-fastapi/
    └── day-05-fastapi/
```

### Day 1

Python fundamentals, strings, basic logic, JSON, configuration files, prompt
loading, and simple AI request examples.

Location: `week-01-python-fastapi/day-01-python-basics/`

### Day 2

Prompt utilities and configuration management using JSON files.

Location: `week-01-python-fastapi/day-02-python/`

### Day 3

Asynchronous Python, simulated AI requests, request failures, validation, and
resilient error handling.

Location: `week-01-python-fastapi/day-03-python/`

## Running the examples

Use Python 3.10 or newer. Run an individual script from the repository root:

```powershell
python .\week-01-python-fastapi\day-03-python\resilient_ai_app.py
```

For Day 1 or Day 2 scripts, use their path under
`week-01-python-fastapi\day-01-python-basics`,
`week-01-python-fastapi\day-02-python`, and
`week-01-python-fastapi\day-03-python`.

### Day 4

FastAPI application basics, routes, query parameters, and interactive API
documentation.

Location: `week-01-python-fastapi/day-04-fastapi/`

Run the API from the repository root:

```powershell
cd .\week-01-python-fastapi\day-04-fastapi
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

### Day 5

FastAPI prompt management with Pydantic validation, in-memory data, create and
read endpoints, response models, and 404 error handling.

Location: `week-01-python-fastapi/day-05-fastapi/`

Run the API from the repository root:

```powershell
cd .\week-01-python-fastapi\day-05-fastapi
uvicorn main:app --reload
```

Available endpoints:

- `POST /prompts` creates a prompt.
- `GET /prompts` returns all prompts.
- `GET /prompts/{prompt_id}` returns one prompt by ID.

Then open `http://127.0.0.1:8000/docs`.

## Notes

The repository intentionally keeps the original learning-day folders so each
exercise remains easy to find. Local virtual environments, Python caches, and
compiled files are excluded from Git.

# AI Engineering Roadmap

Python learning exercises for the first three days of the AI engineering
roadmap.

## Repository structure

```text
.
├── day-03-python/
│   ├── ai_request_simulator.py
│   ├── async_basics.py
│   ├── async_requests.py
│   ├── config_loader.py
│   ├── exceptions.py
│   ├── prompt_manager_v3.py
│   └── resilient_ai_app.py
└── week-01-python-fastapi/
    └── day-01-python-basics/
        └── day-02-python/
```

### Day 1

Python fundamentals, strings, basic logic, JSON, configuration files, prompt
loading, and simple AI request examples.

Location: `week-01-python-fastapi/day-01-python-basics/`

### Day 2

Prompt utilities and configuration management using JSON files.

Location: `week-01-python-fastapi/day-01-python-basics/day-02-python/`

### Day 3

Asynchronous Python, simulated AI requests, request failures, validation, and
resilient error handling.

Location: `day-03-python/`

## Running the examples

Use Python 3.10 or newer. Run an individual script from the repository root:

```powershell
python .\day-03-python\resilient_ai_app.py
```

For Day 1 or Day 2 scripts, use their path under
`week-01-python-fastapi\day-01-python-basics`.

## Notes

The repository intentionally keeps the original learning-day folders so each
exercise remains easy to find. Local virtual environments, Python caches, and
compiled files are excluded from Git.

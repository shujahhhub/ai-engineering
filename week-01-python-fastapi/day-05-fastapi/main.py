from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="AI Prompt Management API",
    description="Day 5 FastAPI application for managing AI prompts.",
    version="2.0.0"
)


# --------------------------------------------------
# Temporary in-memory data
# --------------------------------------------------

prompts = [
    {
        "id": 1,
        "topic": "Python",
        "prompt": "Explain Python for AI engineering.",
        "active": True
    },
    {
        "id": 2,
        "topic": "RAG",
        "prompt": "Explain RAG simply.",
        "active": True
    },
    {
        "id": 3,
        "topic": "AI Agents",
        "prompt": "Explain AI agents.",
        "active": False
    }
]


# --------------------------------------------------
# Pydantic Models
# --------------------------------------------------

class PromptCreate(BaseModel):
    topic: str = Field(min_length=2, max_length=50)
    prompt: str = Field(min_length=5, max_length=500)
    active: bool = True


class PromptResponse(BaseModel):
    id: int
    topic: str
    prompt: str
    active: bool


# --------------------------------------------------
# POST - Create a new prompt
# --------------------------------------------------

@app.post("/prompts", response_model=PromptResponse, status_code=201)
def create_prompt(prompt: PromptCreate):

    new_prompt = {
        "id": len(prompts) + 1,
        "topic": prompt.topic,
        "prompt": prompt.prompt,
        "active": prompt.active
    }

    prompts.append(new_prompt)

    return new_prompt


# --------------------------------------------------
# GET - Get all prompts
# --------------------------------------------------

@app.get("/prompts", response_model=list[PromptResponse])
def get_prompts():
    return prompts


# --------------------------------------------------
# GET - Get one prompt by ID
# --------------------------------------------------

@app.get("/prompts/{prompt_id}", response_model=PromptResponse)
def get_prompt(prompt_id: int):

    for prompt in prompts:
        if prompt["id"] == prompt_id:
            return prompt

    raise HTTPException(
        status_code=404,
        detail="Prompt not found"
    )
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="AI Prompt API",
    description="A simple API for managing AI prompts.",
    version="1.0.0"
)


prompts = [
    {
        "id": 1,
        "topic": "Python",
        "prompt": "Explain Python for AI engineering."
    },
    {
        "id": 2,
        "topic": "RAG",
        "prompt": "Explain RAG simply."
    },
    {
        "id": 3,
        "topic": "AI Agents",
        "prompt": "Explain AI agents."
    }
]


class PromptCreate(BaseModel):
    topic: str
    prompt: str


@app.get("/")
def root():

    return {
        "message": "AI Prompt API is running"
    }


@app.get("/prompts")
def get_prompts():

    return prompts


@app.get("/prompts/search")
def search_prompts(topic: str):

    results = []

    for prompt in prompts:

        if prompt["topic"].lower() == topic.lower():
            results.append(prompt)

    return results


@app.get("/prompts/{prompt_id}")
def get_prompt(prompt_id: int):

    for prompt in prompts:

        if prompt["id"] == prompt_id:
            return prompt

    raise HTTPException(
        status_code=404,
        detail="Prompt not found"
    )


@app.post("/prompts", status_code=201)
def create_prompt(prompt: PromptCreate):

    new_prompt = {
        "id": len(prompts) + 1,
        "topic": prompt.topic,
        "prompt": prompt.prompt
    }

    prompts.append(new_prompt)

    return new_prompt
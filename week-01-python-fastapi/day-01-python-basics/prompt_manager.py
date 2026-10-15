prompts = [
    {
        "id": 1,
        "topic": "Docker",
        "prompt": "Explain Docker to a beginner."
    },
    {
        "id": 2,
        "topic": "RAG",
        "prompt": "Explain RAG with a real-world example."
    },
    {
        "id": 3,
        "topic": "AI Agents",
        "prompt": "What can an AI agent do?"
    }
]


def show_prompts(prompts):
    print("----- AVAILABLE PROMPTS -----")

    for prompt in prompts:
        print(f"{prompt['id']} - {prompt['topic']}")


def get_prompt_by_id(prompts, prompt_id):

    for prompt in prompts:

        if prompt["id"] == prompt_id:
            return prompt

    return None


show_prompts(prompts)

user_choice = int(input("\nEnter prompt ID: "))

selected_prompt = get_prompt_by_id(prompts, user_choice)

if selected_prompt:
    print("\n----- SELECTED PROMPT -----")
    print(f"Topic: {selected_prompt['topic']}")
    print(f"Prompt: {selected_prompt['prompt']}")
else:
    print("Prompt not found.")
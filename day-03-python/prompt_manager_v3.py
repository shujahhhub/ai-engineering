prompts = [
    {
        "id": 1,
        "topic": "Docker",
        "prompt": "Explain Docker simply."
    },
    {
        "id": 2,
        "topic": "RAG",
        "prompt": "Explain RAG simply."
    },
    {
        "id": 3,
        "topic": "AI Agents",
        "prompt": "Explain AI agents simply."
    }
]


def show_prompts(prompts):

    print("\n----- AVAILABLE PROMPTS -----")

    for prompt in prompts:
        print(f"{prompt['id']} - {prompt['topic']}")


def get_prompt_by_id(prompts, prompt_id):

    for prompt in prompts:

        if prompt["id"] == prompt_id:
            return prompt

    return None

    show_prompts(prompts)

try:
    user_choice = int(input("\nEnter prompt ID: "))

except ValueError:
    print("\nInvalid input. Please enter a numeric ID.")

else:
    selected_prompt = get_prompt_by_id(prompts, user_choice)

    if selected_prompt:
        print("\n----- SELECTED PROMPT -----")
        print(f"Topic: {selected_prompt['topic']}")
        print(f"Prompt: {selected_prompt['prompt']}")

    else:
        print("\nPrompt not found.")
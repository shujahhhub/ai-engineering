from prompt_utils import (
    load_prompts,
    show_prompts,
    get_prompt_by_id
)


prompts = load_prompts("prompts.json")

show_prompts(prompts)

user_choice = int(input("\nEnter prompt ID: "))

selected_prompt = get_prompt_by_id(prompts, user_choice)


if selected_prompt:
    print("\n----- SELECTED PROMPT -----")
    print(f"Topic: {selected_prompt['topic']}")
    print(f"Prompt: {selected_prompt['prompt']}")
else:
    print("\nPrompt not found.")
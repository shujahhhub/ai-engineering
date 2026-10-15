import json


def load_prompts(filename):
    with open(filename, "r") as file:
        return json.load(file)


def show_prompts(prompts):
    print("\n----- AVAILABLE PROMPTS -----")

    for prompt in prompts:
        print(f"{prompt['id']} - {prompt['topic']}")


def get_prompt_by_id(prompts, prompt_id):
    for prompt in prompts:
        if prompt["id"] == prompt_id:
            return prompt

    return None
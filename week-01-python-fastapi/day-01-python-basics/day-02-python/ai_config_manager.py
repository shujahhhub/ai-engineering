import json


config = {
    "provider": "OpenAI",
    "model": "gpt-model",
    "settings": {
        "temperature": 0.7,
        "max_tokens": 500,
        "streaming": True
    }
}


def display_config(config):
    print("\n----- AI CONFIGURATION -----")
    print(f"Provider: {config['provider']}")
    print(f"Model: {config['model']}")
    print(f"Temperature: {config['settings']['temperature']}")
    print(f"Max Tokens: {config['settings']['max_tokens']}")
    print(f"Streaming: {config['settings']['streaming']}")


def save_config(config, filename):
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)


def load_config(filename):
    with open(filename, "r") as file:
        return json.load(file)


display_config(config)

save_config(config, "ai_config.json")

loaded_config = load_config("ai_config.json")

print("\nConfiguration loaded from JSON:")

display_config(loaded_config)
import json


config = {
    "provider": "OpenAI",
    "model": "gpt-model",
    "temperature": 0.7,
    "streaming": True
}


with open("config.json", "w") as file:
    json.dump(config, file, indent=4)
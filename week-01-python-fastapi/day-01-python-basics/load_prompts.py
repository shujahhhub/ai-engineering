import json


with open("prompts.json", "r") as file:
    prompts = json.load(file)


print(prompts)

print(type(prompts))
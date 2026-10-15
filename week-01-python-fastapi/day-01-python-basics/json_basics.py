import json


request = {
    "model": "gpt-model",
    "temperature": 0.7,
    "stream": True
}

json_request = json.dumps(request)

print(json_request)

print(type(request))
print(type(json_request))

json_request = json.dumps(request, indent=4)

print(json_request)

{
    "model": "gpt-model",
    "temperature": 0.7,
    "stream": true
}
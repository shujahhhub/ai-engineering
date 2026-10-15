provider = "OpenAI"
model = "gpt-model"
user_prompt = "Explain RAG in simple words."
temperature = 0.7
streaming = True


request = {
    "provider": provider,
    "model": model,
    "prompt": user_prompt,
    "temperature": temperature,
    "streaming": streaming
}


def display_request(request):
    print("----- AI REQUEST -----")
    print(f"Provider: {request['provider']}")
    print(f"Model: {request['model']}")
    print(f"Prompt: {request['prompt']}")
    print(f"Temperature: {request['temperature']}")
    print(f"Streaming: {request['streaming']}")


if request["prompt"].strip():
    display_request(request)
else:
    print("Error: Prompt cannot be empty.")
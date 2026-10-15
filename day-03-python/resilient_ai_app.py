import asyncio


async def send_request(request):

    model = request["model"]
    prompt = request["prompt"]
    delay = request["delay"]
    should_fail = request["should_fail"]

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    print(f"Sending request to {model}...")

    await asyncio.sleep(delay)

    if should_fail:
        raise RuntimeError(
            f"{model} failed to process the request."
        )

    return {
        "model": model,
        "status": "success",
        "response": f"Simulated answer for: {prompt}"
    }


async def process_request(request):

    try:
        return await send_request(request)

    except ValueError as error:
        return {
            "model": request["model"],
            "status": "validation_error",
            "error": str(error)
        }

    except RuntimeError as error:
        return {
            "model": request["model"],
            "status": "request_error",
            "error": str(error)
        }


requests = [
    {
        "model": "Model A",
        "prompt": "Explain Docker.",
        "delay": 2,
        "should_fail": False
    },
    {
        "model": "Model B",
        "prompt": "Explain RAG.",
        "delay": 1,
        "should_fail": True
    },
    {
        "model": "Model C",
        "prompt": "",
        "delay": 2,
        "should_fail": False
    }
]


async def main():

    tasks = []

    for request in requests:
        tasks.append(process_request(request))

    results = await asyncio.gather(*tasks)

    print("\n----- RESULTS -----")

    for result in results:

        if result["status"] == "success":
            print(
                f"{result['model']} SUCCESS: "
                f"{result['response']}"
            )

        else:
            print(
                f"{result['model']} ERROR: "
                f"{result['error']}"
            )


asyncio.run(main())
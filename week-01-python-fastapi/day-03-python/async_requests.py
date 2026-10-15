import asyncio


async def call_ai(model, delay):

    print(f"Sending request to {model}...")

    await asyncio.sleep(delay)

    print(f"Response received from {model}")

    return f"{model} response"


async def main():
    response1 = await call_ai("Model A", 2)
    response2 = await call_ai("Model B", 2)

    print(response1)
    print(response2)


asyncio.run(main())
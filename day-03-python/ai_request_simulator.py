import asyncio


async def send_ai_request(model, should_fail=False):

    print(f"Sending request to {model}...")

    await asyncio.sleep(1)

    if should_fail:
        raise RuntimeError(f"{model} request failed.")

    return f"Response from {model}"


async def main():
    try:
        response = await send_ai_request(
            "Model A",
            should_fail=True
        )

        print(response)

    except RuntimeError as error:
        print(f"Error: {error}")


asyncio.run(main())
import asyncio


async def get_data(name, delay):

    if not name.strip():
        raise ValueError("Name required.")

    await asyncio.sleep(delay)

    return f"Finished {name}"


async def safe_get(name, delay):

    try:
        return await get_data(name, delay)

    except ValueError as error:
        return f"Error: {error}"


async def main():

    results = await asyncio.gather(
        safe_get("A", 2),
        safe_get("", 3),
        safe_get("C", 1)
    )

    print(results)


asyncio.run(main())
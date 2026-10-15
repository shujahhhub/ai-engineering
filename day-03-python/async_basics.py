import asyncio


async def main():
    print("Starting")

    await asyncio.sleep(2)

    print("Finished")


asyncio.run(main())
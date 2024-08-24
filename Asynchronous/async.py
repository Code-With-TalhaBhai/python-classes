import asyncio
import time


async def first(sec):
    await asyncio.sleep(sec)
    # time.sleep(sec)
    print("first function executed")


async def second(sec):
    await asyncio.sleep(sec)
    # time.sleep(sec)
    print("second function executed")


async def third(sec):
    await asyncio.sleep(sec)
    # time.sleep(sec)
    print("third function executed")


async def main():

    L = await asyncio.gather(
    first(3),
    second(2),
    third(1),
    )


asyncio.run(main())



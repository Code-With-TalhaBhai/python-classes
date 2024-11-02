import asyncio


async def my_generator():
    print('start')
    for i in range(5):
        await asyncio.sleep(2)
        yield i
    print('end')
    


async def main():
    async for generator in my_generator():
        print(generator)

    print('after')

asyncio.run(main())

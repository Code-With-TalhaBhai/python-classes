import asyncio


async def main():
    print('starting main')
    await asyncio.sleep(2)
    print('program ending')


asyncio.run(main())


print('how are you')
print('I am fine')
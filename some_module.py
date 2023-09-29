import asyncio


def blocking_task():
    asyncio.run(some_fun())


async def some_fun():
    print('функция запущена')
    await asyncio.sleep(10)
    print('функция отработала')
import asyncio

#
# def blocking_task():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#
#     loop.run_until_complete(some_fun())
#     loop.close()
#
#
# async def some_fun():
#     print('функция запущена')
#     await asyncio.sleep(10)
#     print('функция отработала')


from concurrent.futures import ThreadPoolExecutor
import time


async def blocking_task():
    with ThreadPoolExecutor() as executor:
        try:
            done, pending = await asyncio.wait([asyncio.get_running_loop().run_in_executor(executor, some_fun)])
        except Exception as exc:
            print(f"Произошла ошибка: {exc}")


def some_fun():
    print('функция запущена')
    time.sleep(10)
    print('функция отработала')
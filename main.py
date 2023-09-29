import asyncio
import concurrent.futures

from fastapi import FastAPI

from some_module import blocking_task

app = FastAPI()
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)


@app.get("/")
async def root():
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, blocking_task)

    return {"message": "Hello World"}

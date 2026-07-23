import requests
from threading import Thread
import time
import aiohttp
import asyncio

urls = ["https://postman-echo.com/delay/2"]*5


#

def request_sync():

    start_time = time.time()
    json_list = []

    for url in urls:
        response = requests.get(url).json()
        json_list.append(response)



    end_time = time.time()
    print(f"Total time taken: {end_time - start_time}")

def request_async():
    start_time = time.time()
    json_list = []

    threads = []
    for url in urls:
        thread = Thread(target=lambda: json_list.append(requests.get(url).json()))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time}")



async def request_asyncio():
    st = time.time()

    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.json()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        json_list = await asyncio.gather(*tasks)

    et = time.time()
    print(f"Total time taken: {et-st}")
    return json_list
if __name__ == "__main__":
    asyncio.run(request_asyncio())

import httpx
import sys
from bs4 import BeautifulSoup
import time
import asyncio
import threading
import functools

async def download_without_async(url):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, functools.partial(httpx.get,url))
    file_name = f'./{url.split("/")[-1]}'

    with open(file_name,'w') as f:
        print(response.text,file=f)

async def download(url):
    print("start",url)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    file_name = f'./{url.split("/")[-1]}'

    with open(file_name,'w') as f:
        print(response.text,file=f)

async def main():

    start = time.perf_counter()
    url ="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_a = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]    


    tasks = [download(u) for u in all_a]
    await asyncio.gather(*tasks)

    print(time.perf_counter()-start)

    
if __name__ == '__main__':
    asyncio.run(main())



 
 
 
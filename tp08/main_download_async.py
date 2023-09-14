import httpx
from bs4 import BeautifulSoup
import time
import asyncio


async def download(url_log,sem):
    async with sem:
        print("start",url_log)
        async with httpx.AsyncClient() as client:
            response = await client.get(url_log)
            file_log = url_log.split('/')[-1]
            with  open(file_log,'w') as f: 
                f.write(response.text) 
            
async def main():

    start=time.perf_counter()
    url="https://logs.eolem.com/"
    sem = asyncio.Semaphore(20)
    
    response = httpx.get(url)

    html =response.text
    soup = BeautifulSoup(html, 'html.parser')

    all_a = [url+link.get('href') for link in soup.find_all('a') if ".log" in link.get('href') ] 
    all_download = []


    for d in all_a:
        print(d)
        all_download.append(download(d,sem))
    
    await asyncio.gather(*all_download)
    
    print("time",time.perf_counter()-start)

if __name__=='__main__':
    asyncio.run(main())

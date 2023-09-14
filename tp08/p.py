import time
from bs4 import BeautifulSoup
import asyncio
import httpx

async def download(download_queue:asyncio.Queue, save_queue:asyncio.Queue):
    while True:
        url_log = await download_queue.get()
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url_log)
            to_save = {
                "text": response.text,
                "file_log": url_log.split('/')[-1]
            }            
            save_queue.put_nowait(to_save)
            
        download_queue.task_done()
            
        
async def save(save_queue:asyncio.Queue):
    while True:
        data = await save_queue.get()
        
        with open(data["file_log"], 'w') as f:
            f.write(data["text"])        
        
        save_queue.task_done()


        
async def main():
    start =time.perf_counter()
    
    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    
    
    url = "https://logs.eolem.com/"
    r = httpx.get(url)
    # print(r.text)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    links = [f"{url}{link.get('href')}" for link in soup.find_all('a') if ".log" in link.get('href')]  
        
    # Creation du pool de workers de telechargement
    nb_download_workers = 5   
    download_tasks = []
    for i in range(nb_download_workers):
        task = asyncio.create_task(download(download_queue, save_queue))
        download_tasks.append(task)
    
    # Creation du pool de workers pour l'ecriture
    nb_save_workers = 3
    save_tasks = []
    for i in range(nb_save_workers):
        task = asyncio.create_task(save(save_queue))
        save_tasks.append(task)
    
    for url in links:
        download_queue.put_nowait(url)    
        
    await download_queue.join()
    await save_queue.join()
    
    [d.cancel() for d in download_tasks]
    [d.cancel() for d in save_tasks]
        
        
        
    print("time", time.perf_counter()-start)

if __name__=='__main__':
    asyncio.run(main())
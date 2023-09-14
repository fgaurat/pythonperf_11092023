
import requests
from bs4 import BeautifulSoup
import time
import threading
from multiprocessing.pool import ThreadPool

def download(url_log):
    response = requests.get(url_log)
    file_log = url_log.split('/')[-1]
    with  open(file_log,'w') as f: 
        f.write(response.text) 
        
def main():
    start=time.perf_counter()
    url="https://logs.eolem.com/"

    response = requests.get(url)
    html =response.text
    soup = BeautifulSoup(html, 'html.parser')

    all_a = [url+link.get('href') for link in soup.find_all('a') if ".log" in link.get('href') ] 

    with ThreadPool(10) as tp:
        tp.map(download,all_a)

    
    print("time",time.perf_counter()-start)

if __name__=='__main__':
    main()



    a = [1,2,3,4]

    l = map(lambda i:i*2,a)
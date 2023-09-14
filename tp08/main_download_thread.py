import requests
from bs4 import BeautifulSoup
import time
import threading


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


    threads = []
    for url_log in all_a:
        th1 = threading.Thread(target=download,args=[url_log])
        th1.start()
        threads.append(th1)
        # download(url_log)

    for th in threads:
        th.join()
    print("time",time.perf_counter()-start)

if __name__=='__main__':
    main()

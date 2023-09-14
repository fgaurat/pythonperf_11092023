import requests
from bs4 import BeautifulSoup
import time


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

    for url_log in all_a:
        download(url_log)


    print("time",time.perf_counter()-start)

if __name__=='__main__':
    main()

from collections.abc import Callable, Iterable, Mapping
import time
import threading
from typing import Any

the_lock = threading.Lock()

def traitement_long_1():
    with the_lock:
        for i in range(5):
            print(f"traitement_long_1 {i} - {threading.current_thread()}")
            time.sleep(0.3)

def traitement_long_2():
    with the_lock:
        for i in range(5):
            print(f"traitement_long_2 {i} - {threading.current_thread()}")
            time.sleep(0.3)

class TheThread(threading.Thread):

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        with the_lock:
            for i in range(5):
                print(f"run {i} - {self.name}")
                time.sleep(0.3)


                
def main():

    th1 = TheThread()
    th2 = TheThread()
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print("fin threads")


def main01():
    th1 = threading.Thread(target=traitement_long_1)
    th2 = threading.Thread(target=traitement_long_2)

    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print("fin threads")

if __name__=='__main__':
    main()

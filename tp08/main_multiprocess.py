from multiprocessing import Pool
import time
import os
def f(x):
    t = 1
    start = time.time()
    while time.time()-start<t:
        pass
    return x*x

def main():
    print(os.cpu_count())
    with Pool() as p:
        print(p.map(f, range(1,30)))

if __name__=='__main__':
    start = time.perf_counter()
    main()
    print(time.perf_counter()-start)

import time
from functools import lru_cache

@lru_cache(maxsize = 32)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now running some time")
    some_work(3)
    some_work(4)
    some_work(2)
    some_work(1)
    print("done....celling again ")
    some_work(3)
    print("called again")
import time
from functools import lru_cache

print("how many value would like to cache ")
c1 = int(input())
@lru_cache(maxsize=c1)
def mobile_num(c1):
    time.sleep(c1)
    return c1

mobile_num(4)
print("loading found")
mobile_num(5)
print("found your number")
mobile_num(7)
print("found is done")








''' 
Function Caching :
Save results of function calls so repeated calls with the same inputs are faster.
'''

from functools import lru_cache
import time

@lru_cache(maxsize = None)
def fx(num):
    time.sleep(3)
    return num * 3

print(fx(3))
print(fx(9))

print(fx(3))
print(fx(9))

print(fx(6))

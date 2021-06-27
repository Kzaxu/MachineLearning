import numpy as np 
import math 
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time 

PRIMES = [112272535095293] * 100

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True 
    elif n % 2 == 0:
        return False
    sqrt_n = math.floor(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True 

def single_thread():
    for n in PRIMES:
        is_prime(n)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES) 

# 多进程必须在 __name__ == "__main__" 下使用
def multi_proc():
    with ProcessPoolExecutor() as pool:
        result = pool.map(is_prime, PRIMES) 
    return result

if __name__ == "__main__":
    bg = time.time()
    multi_proc()
    ed = time.time()
    print(f"multi process cost time {round(ed-bg, 3)}s")
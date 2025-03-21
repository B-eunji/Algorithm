import sys
import math

input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i ==0:
            return False
    return True

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    while not is_prime(n):
        n+=1
    print(n)
import sys

N = int(sys.stdin.readline())
numbers_N = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers_M = list(map(int,sys.stdin.readline().split()))

for num in numbers_M:
    if num in numbers_N:
        print(1, end=' ')
    else:
        print(0, end=' ')
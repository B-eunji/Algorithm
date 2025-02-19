import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip()) #자료구조의 개수
A = list(map(int,input().split())) #수열 A
B = list(map(int, input().split())) #수열 B
M = int(input().strip()) #삽입 할 수열의 길이
C = list(map(int,input().split())) #삽입 할 수열

queue = deque()
for i in range(N):
    if A[i] == 0:
        queue.appendleft(B[i])

queue.extend(C)

for _ in range(M):
    print(queue.popleft(), end=" ")
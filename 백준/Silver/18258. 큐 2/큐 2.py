import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
queue = deque()

for _ in range(N):
    com = input().strip().split()
    
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        print(0 if queue else 1)
    elif com[0] == 'front':
        print(queue[0] if queue else -1)
    elif com[0] == 'back':
        print(queue[-1] if queue else -1)
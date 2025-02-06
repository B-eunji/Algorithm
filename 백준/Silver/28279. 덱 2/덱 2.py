import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
queue = deque()

for _ in range(N):
    com_num = input().strip().split()
    
    if com_num[0] == '1':
        queue.appendleft(int(com_num[1]))
    elif com_num[0] == '2':
        queue.append(int(com_num[1]))
    elif com_num[0] == '3':
        print(queue.popleft() if queue else -1)
    elif com_num[0] == '4':
        print(queue.pop() if queue else -1)
    elif com_num[0] == '5':
        print(len(queue))
    elif com_num[0] == '6':
        print(1 if not queue else 0)
    elif com_num[0]=='7':
        print(queue[0] if queue else -1)
    elif com_num[0]=='8':
        print(queue[-1] if queue else -1)          

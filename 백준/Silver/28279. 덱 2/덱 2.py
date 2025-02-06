import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())  # 명령 개수 입력
deque_obj = deque()  # 덱(Deque) 생성

for _ in range(N):
    command = input().strip().split()  # 명령 입력 받기
    
    if command[0] == '1':  # push_front X
        deque_obj.appendleft(int(command[1]))
    elif command[0] == '2':  # push_back X
        deque_obj.append(int(command[1]))
    elif command[0] == '3':  # pop_front
        print(deque_obj.popleft() if deque_obj else -1)
    elif command[0] == '4':  # pop_back
        print(deque_obj.pop() if deque_obj else -1)
    elif command[0] == '5':  # size
        print(len(deque_obj))
    elif command[0] == '6':  # empty (1 if empty, 0 otherwise)
        print(1 if not deque_obj else 0)
    elif command[0] == '7':  # front
        print(deque_obj[0] if deque_obj else -1)
    elif command[0] == '8':  # back
        print(deque_obj[-1] if deque_obj else -1)
        
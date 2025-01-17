import sys

input = sys.stdin.readline
N = int(input().strip())
stack = []

for _ in range(N):
    op = input().strip().split()
    
    if op[0] == '1':  # push
        stack.append(int(op[-1]))
        continue
    elif op[0] == '2':  # pop
        if stack:
            print(stack.pop())
            continue
        print(-1)
    elif op[0] == '3':  # size
        print(len(stack))
        continue
    elif op[0] == '4':  # empty
        if stack:
            print(0)
            continue
        print(1)
    elif op[0] == '5':  # top
        if stack:
            print(stack[-1])
            continue
        print(-1)
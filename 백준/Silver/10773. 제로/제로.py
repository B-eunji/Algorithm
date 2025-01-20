import sys

K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)
print(sum(stack))
import sys
input = sys.stdin.readline

N = int(input().strip())
queue = list(map(int,input().strip().split()))
stack = []
current = 1

while queue or stack:
    if queue and queue[0] == current:
        queue.pop(0)
        current += 1
    elif stack and stack[-1] == current:
        stack.pop()
        current += 1
    elif queue:
        stack.append(queue.pop(0))
    else:
        print("Sad")
        break
else:
    print("Nice")
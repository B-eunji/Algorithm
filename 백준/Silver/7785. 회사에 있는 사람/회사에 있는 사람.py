import sys

n = int(sys.stdin.readline())
data = set()

for _ in range(n):
    name, action = sys.stdin.readline().split()
    if action == "enter":
        data.add(name)
    elif action == "leave":
        data.discard(name)

for name in sorted(data, reverse=True):
    print(name)
    
import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
balloons = deque(enumerate(map(int,input().split()), start=1))

result = []

while balloons:
    index, num = balloons.popleft()
    result.append(index)
    
    if balloons:
        if num > 0:
            balloons.rotate(-(num-1))
        else:
            balloons.rotate(-num)


print(" ".join(map(str, result)))

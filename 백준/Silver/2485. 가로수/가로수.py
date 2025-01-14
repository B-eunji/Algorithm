import sys
import math

input = sys.stdin.readline

N = int(input())
positions = [int(input()) for _ in range(N)]

distances = [positions[i+1] - positions[i] for i in range(N-1)]

gcd = distances[0]
for d in distances[1:]:
    gcd = math.gcd(gcd,d)
    
additional_trees = sum((d//gcd-1) for d in distances)

print(additional_trees)

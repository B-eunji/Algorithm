import sys

input = sys.stdin.readline

N,M = map(int, input().split())

N_names = {input().strip() for _ in range(N)}
M_names = {input().strip() for _ in range(M)}
    
names = N_names & M_names
print(len(names))
for name in sorted(names):
    print(name)
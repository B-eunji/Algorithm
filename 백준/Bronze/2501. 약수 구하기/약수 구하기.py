N,K = map(int,input().split())
out = []

for i in range(1, N+1):
    if N % i == 0:
        out.append(i)
if len(out) >= K:
    print(out[K-1])
else:
    print(0)
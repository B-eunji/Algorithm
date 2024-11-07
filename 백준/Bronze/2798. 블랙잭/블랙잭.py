N,M = map(int,input().split())
cards = list(map(int,input().split()))

max_sum = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            current_max = cards[i] + cards[j] + cards[k]
            if current_max <= M:
                max_sum = max(max_sum, current_max)
print(max_sum)
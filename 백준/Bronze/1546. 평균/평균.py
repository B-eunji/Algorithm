N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
result = []
for i in range(N):
    result.append(score[i]/max_score*100)
print(sum(result)/N)
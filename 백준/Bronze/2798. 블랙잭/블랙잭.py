N, M = map(int, input().split())
nums = list(map(int, input().split()))

best = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_value = nums[i] + nums[j] + nums[k]

            if sum_value <= M:
                best = max(best, sum_value)

print(best)
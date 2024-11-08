N = int(input())
result = 0

for i in range(max(1, N - len(str(N)) * 9), N):
    decomposition_sum = i + sum(int(digit) for digit in str(i))
    if decomposition_sum == N:
        result = i
        break

print(result)
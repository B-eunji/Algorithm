N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
    
A.sort()

for num in A:
    print(num)
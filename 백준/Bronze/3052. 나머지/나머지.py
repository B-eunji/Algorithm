numbers = set()

for _ in range(10):
    N = int(input())
    numbers.add(N % 42)
    
print(len(numbers))
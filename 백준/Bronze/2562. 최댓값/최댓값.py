numbers = 0
numbers_idx = 0
for i in range(9):
    num = int(input())
    if numbers < num:
        numbers = num
        numbers_idx = i + 1
print(numbers)
print(numbers_idx)
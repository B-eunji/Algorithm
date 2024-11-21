
A = []
for _ in range(5):
    num = int(input())
    A.append(num)

average = sum(A)//len(A)

A.sort()
middle_output = A[len(A) // 2]
    
print(average)
print(middle_output)

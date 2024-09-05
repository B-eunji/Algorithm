A = input()

if A[0] == 'F':
    first_num = 0
    second_num = 0
elif A[1] == '+':
    second_num = 3
    if A[0] == 'A':
        first_num = 4
    elif A[0] == 'B':
        first_num = 3
    elif A[0] == 'C':
        first_num = 2
    elif A[0] == 'D':
        first_num = 1
elif A[1] == '0':
    second_num = 0
    if A[0] == 'A':
        first_num = 4
    elif A[0] == 'B':
        first_num = 3
    elif A[0] == 'C':
        first_num = 2
    elif A[0] == 'D':
        first_num = 1
elif A[1] == '-':
    second_num = 7
    if A[0] == 'A':
        first_num = 3
    elif A[0] == 'B':
        first_num = 2
    elif A[0] == 'C':
        first_num = 1
    elif A[0] == 'D':
        first_num = 0

print(str(first_num) + '.' + str(second_num))
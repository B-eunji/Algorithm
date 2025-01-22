T = int(input())

for _ in range(T):
    stack = []
    is_valid  = True
    x = input().strip()
    
    for char in x:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break

    if is_valid and not stack:
        print('YES')
    else:
        print('NO')
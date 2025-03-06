H,M = map(int,input().split())


if M < 45:
    H = H-1 if H > 0 else 23
    M = M-45+60
else:
    M = M - 45

print(H,M)
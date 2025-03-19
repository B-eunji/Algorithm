import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T+1):
    case_n = "Case #" + str(i) + ": "
    A,B = map(int,input().split())
    C = A+B
    print(case_n + str(C))
X = int(input()) # 영수증 총 금액
N = int(input()) # 영수증 물건 종류의 수

coin = 0
for i in range(1,N+1): #(1,N+1) -> N
    a,b = map(int,input().split())
    coin += a*b
    
if (coin==X):
    print("Yes")
else:
    print("No")
     
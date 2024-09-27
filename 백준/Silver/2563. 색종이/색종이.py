N = int(input())
matrix = [[0]*100 for _ in range(100) ]

for i in range(N):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            matrix[i][j] = 1
            
area = sum(sum(row) for row in matrix)
print(area)
    
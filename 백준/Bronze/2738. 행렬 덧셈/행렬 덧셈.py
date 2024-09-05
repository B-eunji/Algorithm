
N, M = map(int, input().split())

matrix1 = []
for _ in range(N):
    row = list(map(int,input().split()))
    matrix1.append(row)
    
matrix2 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix2.append(row)
    
result = []    
for i in  range(N):
    row = []
    for j in range(M):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
    
for row in result:
    print(" ".join(map(str, row)))
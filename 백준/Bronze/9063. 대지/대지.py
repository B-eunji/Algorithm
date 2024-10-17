N = int(input())
x_list = []
y_list = []

for i in range(N):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
    
max_x = max(x_list)
min_x = min(x_list)
max_y = max(y_list)
min_y = min(y_list)

result = (max_x - min_x)*(max_y - min_y)
print(result)

N,M = map(int,input().split())
board = [input() for _ in range(N)]

def count_recolor(x,y,start_color):
    count = 0
    for i in range(8):
        for j in range(8):
            expected_color = 'W' if (i+j) % 2 == 0 else 'B'
            if start_color == 'B':
                expected_color = 'B' if expected_color == 'W' else 'W'
            if board[x+i][y+j] != expected_color:
                count += 1
    return count

min_recolor = float('inf')

for i in range(N-7):
    for j in range(M-7):
        min_recolor = min(min_recolor, count_recolor(i,j,'W'), count_recolor(i,j,'B'))
        
print(min_recolor)
            
    
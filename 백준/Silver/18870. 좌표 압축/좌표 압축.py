import sys

N = int(sys.stdin.readline())

coordinates = list(map(int,sys.stdin.readline().split()))

sorted_coord = sorted(set(coordinates))

coord_map = {value: index for index, value in enumerate(sorted_coord)}

result = [coord_map[x] for x in coordinates]
print(*result)
import sys

N = int(sys.stdin.readline())

coordinates = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

coordinates.sort(key=lambda coord: (coord[1], coord[0]))

for coord in coordinates:
    print(coord[0], coord[1])
angles = []

for i in range(3):
    N = int(input())
    angles.append(N)
    
if sum(angles) == 180:
    if angles.count(60) == 3:
        print("Equilateral")
    elif angles.count(angles[0]) == 2 or angles.count(angles[1]) == 2:
        print("Isosceles")    
    else:
        print("Scalene")
else:
    print("Error")
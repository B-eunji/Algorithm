while True:
    A,B,C = map(int,input().split())
    
    if A==0 and B==0 and C==0:
        break
    
    if A+B >C and A+C>B and B+C>A:
        if A == B and B == C and A==C:
            print("Equilateral")
        elif A == B or B == C or A==C:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")
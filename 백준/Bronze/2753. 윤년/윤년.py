A = int(input())
year_1 = A % 4==0 and A % 100 != 0
year_2 = A % 4==0 and A % 400 ==0
if year_1 or year_2:
    print("1")
else:
    print("0")
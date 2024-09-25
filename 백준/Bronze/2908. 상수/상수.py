Num_1, Num_2 = input().split()

Num_1_reversed = int(Num_1[::-1]) 
Num_2_reversed = int(Num_2[::-1])

if Num_1_reversed > Num_2_reversed:
    result = Num_1_reversed
else:
    result = Num_2_reversed
    
print(result)
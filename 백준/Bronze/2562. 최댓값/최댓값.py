num_list = [int(input()) for _ in range(9)] 
max_int = max(num_list)

max_num = num_list.index(max_int) + 1

print(max_int)
print(max_num)
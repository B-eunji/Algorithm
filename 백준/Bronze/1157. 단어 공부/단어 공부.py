words = input().upper()
unique_word = list(set(words))

count_list = []
for char in unique_word:
    count = words.count(char)
    count_list.append(count)
    
if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(unique_word[max_index])
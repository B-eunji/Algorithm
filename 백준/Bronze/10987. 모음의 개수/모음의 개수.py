words = input().strip()
count = [0] * 26

for i in words:
    count[ord(i) - ord('a')] += 1
    
print(count[0] + count[4] + count[8] + count[14] + count[20])

S = input()
alphabet = [-1] * 26

for i in range(len(S)):
    index = ord(S[i]) - ord('a')
    if alphabet[index] == -1:
        alphabet[index] = i

print(" ".join(map(str,alphabet)))    
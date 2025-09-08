S = input()
alphabets = [chr(ord('a')+i) for i in range(26)]

result = []
for ch in alphabets:
    result.append(S.find(ch))

print(*result)

import sys
N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]

unique_words = list(set(words))

unique_words.sort(key=lambda word: (len(word), word))

for word in unique_words:
    print(word)
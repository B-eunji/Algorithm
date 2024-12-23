import sys
from collections import Counter

N = int(sys.stdin.readline())
cards_num = list(sys.stdin.readline().split())
M = int(sys.stdin.readline())
cards_num_M = list(sys.stdin.readline().split())

cards_count = Counter(cards_num)

result = [cards_count[num] for num in cards_num_M]
print(" ".join(map(str, result)))     
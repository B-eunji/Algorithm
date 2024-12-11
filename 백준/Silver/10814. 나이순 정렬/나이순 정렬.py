import sys

N = int(sys.stdin.readline())
members = [tuple(sys.stdin.readline().split()) for _ in range(N) ]

members = [(int(age), name) for age, name in members]

members.sort(key=lambda member:member[0])

for age, name in members:
    print(age,name)
import sys

A,B = map(int,sys.stdin.readline().split())
A_numbers = set(map(int,sys.stdin.readline().split()))
B_numbers = set(map(int,sys.stdin.readline().split()))

sum_numbers = A_numbers^B_numbers

print(len(sum_numbers))
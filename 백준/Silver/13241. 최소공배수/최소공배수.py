import sys
import math

A,B = map(int,sys.stdin.readline().split())
gcd = math.gcd(A,B)
print(A*B//gcd)
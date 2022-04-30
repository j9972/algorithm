import sys
from math import gcd
input = sys.stdin.readline

a, b = map(int, input().split())

print(gcd(a, b))
print(a*b // gcd(a, b))

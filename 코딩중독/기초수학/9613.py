import sys
from math import gcd
input = sys.stdin.readline

t = int(input())

for i in range(t):
    data = list(map(int, input().split()))
    total = 0

    for j in range(1, len(data)):
        for k in range(j+1, len(data)):
            total += gcd(data[j], data[k])

    print(total)

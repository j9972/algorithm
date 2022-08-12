from math import ceil
import sys
input = sys.stdin.readline

x, y = map(int, input().split())

z = (y/x * 100) % 1
d = 1 - z


if x == y or int((y/x) * 100) == 99:
    a = -1
else:
    a = (x*d) / (100-d-y/x*100)
    a = round(a, 10)
    a = ceil(a)

print(a)

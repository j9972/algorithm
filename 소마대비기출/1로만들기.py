# 실버 3 - 1463
import sys
input = sys.stdin.readline

x = int(input())
d = [0] * (x+1)
d[1] = 0
d[2] = 1
d[3] = 1

for i in range(4, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
print(d[x-1])

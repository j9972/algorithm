# 실버 4 - 2839
import sys
input = sys.stdin.readline

n = int(input())

d = [5001] * (n+1)
d[0] = 0
s = [3, 5]

for i in s:
    for j in range(1, n+1):
        if j - i >= 0:
            d[j] = min(d[j], d[j-i] + 1)


if d[n] != 5001:
    print(d[n])
else:
    print(-1)

# 골드 5 - 2294
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [10001] * (k+1)
d[0] = 0

for i in coin:
    for j in range(i, k+1):
        if j - i >= 0:
            d[j] = min(d[j], d[j-i] + 1)


if d[k] != 10001:
    print(d[k])
else:
    print(-1)

# 골드 5 - 2294
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [10001] * (k+1)
d[0] = 0

for i in range(len(coin)):
    for j in range(coin[i], k+1):
        d[i] = min(d[i], d[j-coin[i]] + 1)


if d[n-1] != 10001:
    print(d[n-1])
else:
    print(-1)

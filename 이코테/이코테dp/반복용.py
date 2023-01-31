# 바닥 공사
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort()

d = [10001] * (m+1)  # 1<=m<=10000
d[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j], d[j-coin[i]]+1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)

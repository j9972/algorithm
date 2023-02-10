import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [10001] * (k+1)
d[0] = 0
for i in range(n):
    for j in range(coin[i], k+1):
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j-coin[i]]+1, d[j])

if d[k] != 10001:
    print(d[k])
else:
    print(-1)

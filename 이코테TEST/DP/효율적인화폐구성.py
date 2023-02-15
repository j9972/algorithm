import sys
input = sys.stdin.readline

n, m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort()

d = [10001] * (m+1)
d[0] = 0

for i in coin:
    for j in range(i, m+1):
        if d[j-i] != 10001:
            d[j] = min(d[j], d[j-i]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

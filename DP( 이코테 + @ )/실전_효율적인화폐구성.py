import sys
input = sys.stdin.readline

n,m = map(int,input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in coin:
    for j in range(i,m+1):
        d[j] = min(d[j], d[j-i]+1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)
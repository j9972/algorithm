import sys
sys.setrecursionlimit(10**7)

n,k = map(int,input().split())

coin = [
    int(input())
    for _ in range(n)
]

d = [sys.maxsize] * (k+1)
d[0] = 0

for i in coin:
    for j in range(1,k+1):
        if j - i >= 0:
            d[j] = min(d[j], d[j-i] + 1)

if d[k] == sys.maxsize:
    print(-1)
else:
    print(d[k])

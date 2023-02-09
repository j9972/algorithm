# 실버 1 - 1495
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
n, start, m = map(int, input().split())
v = list(map(int, input().split()))

d = [[False] * (m+1) for _ in range(n+1)]
d[0][start] = True

for song in range(n):
    for vol in range(m+1):
        if d[song][vol] == True:
            for next in [vol - v[song], vol + v[song]]:
                if 0 <= next <= m:
                    d[song+1][next] = True

res = -1
for vol in range(m, -1, -1):
    if d[n][vol] == True:
        res = vol
        break
print(res)

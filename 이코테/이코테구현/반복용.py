# 치킨 배달
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chicken.append([i, j])
        elif data[i][j] == 1:
            home.append([i, j])

res = 1e9

for ch in combinations(chicken, m):
    temp = 0
    for h in home:
        ch_len = 999
        for j in range(m):
            ch_len = min(ch_len, abs(h[0]-ch[j][0]) + abs(h[1]-ch[j][1]))
        temp += ch_len
    res = min(res, temp)
print(res)

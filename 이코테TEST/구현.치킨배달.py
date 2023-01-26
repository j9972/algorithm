from itertools import combinations as cb
import sys
input = sys.stdin.readline

home = []
chicken = []

n, m = map(int, input().split())

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            home.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))


distance = 1e9
for ch in cb(chicken, m):
    temp = 0
    for h in home:
        ch_len = 999
        for i in range(m):
            ch_len = min(ch_len, abs(h[0] - ch[i][0]) + abs(h[1] - ch[i][1]))
        temp += ch_len
    distance = min(distance, temp)
print(distance)

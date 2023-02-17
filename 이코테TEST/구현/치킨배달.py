from itertools import combinations as cb
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

home = []
chicken = []
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))


dist = 1e9
for ch in cb(chicken, m):
    res = 0
    for hx, hy in home:
        ch_len = 1e9
        for i in range(m):
            ch_len = min(ch_len, abs(hx-ch[i][0]) + abs(hy-ch[i][1]))
        res += ch_len
    dist = min(dist, res)
print(dist)

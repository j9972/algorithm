import sys
input = sys.stdin.readline
from itertools import combinations as cb

n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

dist = int(1e9)
for ch in cb(chicken,m):
    res = 0
    for hx,hy in home:
        ch_len = 1e9
        for i in range(m):
            ch_len = min(ch_len, abs(ch[i][0]- hx) + abs(ch[i][1]- hy))
        res += ch_len
    dist = min(res, dist)
print(dist)
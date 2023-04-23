import sys
input = sys.stdin.readline
from itertools import combinations as cb

n,m = map(int,input().split())

board = []
chicken = []
home = []

for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i,j))
        if board[i][j] == 2:
            chicken.append((i,j))

res = 1e9
for ch in cb(chicken,m):
    tmp = 0
    for h in home:
        ch_len = 999
        for i in range(m):
            ch_len = min(ch_len, abs(h[0] - ch[i][0]) + abs(h[1] - ch[i][1]))
        tmp += ch_len
    res = min(res, tmp)
print(res)
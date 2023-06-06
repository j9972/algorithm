import sys
input = sys.stdin.readline
from itertools import combinations as cb

n,m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

res = 1e9
for i in cb(chicken,m):
    tmp = 0
    for h in home:
        ch_len = 999
        for ch in range(m):
            ch_len = min(ch_len, abs(h[0]-i[ch][0]) + abs(h[1]-i[ch][1]))
        tmp += ch_len
    if tmp < res:
        res = tmp
print(res)
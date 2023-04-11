#1890
import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

d = [[0] * n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):

        if i == j ==n-1:
            print(d[i][j])
            break

        dist = board[i][j]
        if i + dist < n:
            d[i+dist][j] += d[i][j]
        if j + dist < n:
            d[i][j+dist] += d[i][j]
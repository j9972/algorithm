# 골드4 - 9663
import sys
input = sys.stdin.readline

n = int(input())
board = [[0]*(n) for i in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def check(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if board[nx][ny] == 1:
            return False
    return True


cnt = 0


def bfs(n):
    global cnt
    for i in range(n):
        for j in range(n):
            board[i][j] = 1

            if check(i, j):
                cnt += 1

    for i in range(n):
        for j in range(n):
            board[i][j] = 0
    return cnt


print(bfs(n))

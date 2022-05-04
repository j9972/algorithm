# from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(x, y):
    # 대각선 포함
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    countNumList = []
    countNum = 0
    field[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and field[nx][ny] == 1:
            dfs(nx, ny)
            countNum += 1
    countNumList.append(countNum)


while True:
    n = int(input())
    field = []
    count = 0
    for _ in range(n):
        field.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if field[i][j] == 1:
                dfs(i, j)
                count += 1


print(count)

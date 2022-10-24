from collections import deque
import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

resetArray = [[0]*(m+1) for _ in range(n+1)]

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

res = 0


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if resetArray[nx][ny] == 0:
                resetArray[nx][ny] = 2
                virus(nx, ny)


def getScore():
    score = 0
    for i in range(n):
        for j in range(n):
            if resetArray[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global res
    if count == 3:
        for i in range(n):
            for j in range(m):
                resetArray[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if resetArray[i][j] == 2:
                    virus(i, j)
        res = max(res, getScore())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(res)

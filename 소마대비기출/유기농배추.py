# 실버 2 - 1012
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m and veg[x][y] == 1:
        veg[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for tc in range(int(input())):
    n, m, k = map(int, input().split())

    veg = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        veg[x][y] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)

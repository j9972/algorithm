# dfs 영역 문제 -> 음료수 얼려 먹기
# keep
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * (n+1) for _ in range(n+1)]

res = 0


def dfs(x, y):
    for i in range(1, 101):
        if 0 <= x < n and 0 <= y < n and board[x][y] >= i:
            if visited[x][y] == 0:
                visited[x][y] = 1
                board[x][y] = i - 1
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
                return True
        return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            res += 1
print(res)

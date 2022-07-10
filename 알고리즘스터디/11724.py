# dfs 문제
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
count = 0

board = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)


def dfs(now):
    visited[now] = True
    for i in board[now]:
        if not visited[i]:
            dfs(i)


for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)

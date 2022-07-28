import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())


def distance(start, find):
    queue = deque()
    queue.append((start, 0))

    visited = [False] * (n+1)
    visited[start] = True

    while queue:
        v, d = queue.popleft()
        if v == find:
            return d
        for i, l in board[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append((i, d+l))


board = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    board[a].append((b, c))
    board[b].append((a, c))

for _ in range(m):
    a, b = map(int, input().split())
    print(distance(a, b))

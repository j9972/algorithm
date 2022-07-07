# 간선의 길이가 1로 통일 하니 bfs, 최단 시간 찾기
from collections import deque

# 1이동시 x-1 x+1, 순간이동시 2*x

# 수빈이와 동생의 위치
n, k = map(int, input().split())

board = [[] for _ in range(100001)]

visited = [0] * (100001)

for i in range(100001):
    board[i] = [i-1, i+1, i*2]


def bfs(x):
    queue = deque([x])

    if visited[x] > 0:
        return False

    visited[x] = 1

    while queue:
        now = queue.popleft()
        for i in board[now]:
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)

        if now == k:
            return visited[k] - 1
    return True


print(bfs(n))

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def process(x, y, idx):
    united = []
    united.append((x, y))

    queue = deque()
    queue.append((x, y))

    union[x][y] = idx
    summary = graph[x][y]
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx, ny))
                    union[nx][ny] = idx
                    summary = graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        graph[i][j] = summary // count
    return count


total = 0
while True:
    union = [[-1]*n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, idx)
                idx += 1
    if idx == n * n:
        break
    total += 1

print(total)

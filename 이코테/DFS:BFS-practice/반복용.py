from collections import deque

n, l, r = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    union[x][y] = index
    summary = data[x][y]
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    union[nx][ny] = index
                    summary += data[nx][ny]
                    count += 1
                    united.append((nx, ny))
                    q.append((nx, ny))
    for x, y in united:
        data[x][y] = summary // count
    return count


tot = 0
while True:
    union = [[-1] * (n+1) for _ in range(n+1)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == n*n:
        break
    tot += 1

print(tot)

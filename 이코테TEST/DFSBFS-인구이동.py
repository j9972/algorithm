from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def process(x, y, index):

    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    summary = data[x][y]
    union[x][y] = index
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    cnt += 1
                    summary += data[nx][ny]
                    union[nx][ny] = index
                    united.append((nx, ny))
                    q.append((nx, ny))
    for x, y in united:
        data[x][y] = summary // cnt
    return cnt


tot = 0
while True:
    index = 0
    union = [[-1] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                index += 1
                process(i, j, index)
    if index == n*n:
        break
    tot += 1

print(tot)

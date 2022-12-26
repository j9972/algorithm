from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


virusData = []

data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virusData.append((data[i][j], 0, i, j))
virusData.sort()
q = deque(virusData)

tar_s, tar_x, tar_y = map(int, input().split())

while q:
    virus, s, x, y = q.popleft()

    if s == tar_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
print(data[tar_x-1][tar_y-1])

from collections import deque
import sys
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

otherArray = []

data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            otherArray.append((data[i][j], 0, i, j))

otherArray.sort()
queue = deque(otherArray)

s, x, y = map(int, input().split())

while queue:
    virus, target_s, target_x, target_y = queue.popleft()

    if s == target_s:
        break

    for i in range(4):
        nx = target_x + dx[i]
        ny = target_y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                queue.append((virus, target_s+1, nx, ny))

print(data[x-1][y-1])

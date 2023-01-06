from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())

graph = []
data = []  # 처음 입력을 받는 파트
for x in range(n):
    data.append(list(map(int, input().split())))
    for y in range(n):
        if data[x][y] != 0:
            graph.append((data[x][y], 0, x, y))  # 바이러스 , 시간, x, y 좌표 넣기

graph.sort()
q = deque(graph)

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

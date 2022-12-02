
from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 상황을 보여줌
data = []  # virus 정보를 담을 배열

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # data 는 바이러스의 대한 정보만을 담고 있기에 graph에서 바이러스에 대한 정보를 다 담아준다.
            data.append((graph[i][j], 0, i, j))


data.sort()
queue = deque(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tarS, tarX, tarY = map(int, input().split())

while queue:
    virus, s, x, y = queue.popleft()
    if s == tarS:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            # 전체 정보가 담겨져 있는 배열에서 전염될수 있는 부분 체크해서 queue에 넣어줘서 while문을 돌린다
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(graph[tarX-1][tarY-1])

# bfs문제인 이유는 0,0에서 시작하고 간선의 길이가 다 같기때문
from collections import deque

n, m = map(int, input().split())

# 2차원 리스트 맵을 이런식으로 줘도 되는 이유는 후에 변수를 받지 않고 맵의 정보를 통해서만 문제를 풀기 때문
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    # 시작의 위치를 queue에 넣어줘야 한다
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # 이동한 곳의 위치값으 변경해줘서 값이 증진하는 것을 알 수 있다.
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0, 0))

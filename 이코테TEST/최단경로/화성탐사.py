import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(int(input())):
    n = int(input())
    INF = int(1e9)
    graph = [[INF] * n for _ in range(n)]

    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    x, y = 0, 0
    graph[x][y] = data[x][y]
    q = [(graph[x][y], x, y)]

    while q:
        dist, x, y = heapq.heappop(q)

        if graph[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + data[nx][ny]
                if cost < graph[nx][ny]:
                    graph[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(graph[n-1][n-1])

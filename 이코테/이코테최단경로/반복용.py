# 정확한순위 - 플로이드
import sys
import heapq
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(1e9)

for tc in range(int(input())):
    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF]*n for _ in range(n)]

    x, y = 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if distance[nx][ny] < dist:
                continue
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])

# 화성탐사 -> 개선된 다익스트라 ( 1번 노드로부터 모든 노드의 최단거리를 구하므로 )
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(input())):
    n = int(input())
    distance = [[INF]*n for _ in range(n)]

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])

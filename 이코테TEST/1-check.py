import heapq
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())

    INF = int(1e9)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph = [[INF]*(n+1) for _ in range(n+1)]

    costData = []
    for i in range(n):
        costData.append(list(map(int, input().split())))

    q = []
    x, y = 0, 0
    heapq.heappush(q, (costData[x][y], x, y))
    graph[x][y] = costData[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if dist > graph[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + costData[nx][ny]
                if cost < graph[nx][ny]:
                    graph[nx][ny] = cost
                    heapq.heappush(q, (graph[nx][ny], nx, ny))
    print(graph[n-1][n-1])

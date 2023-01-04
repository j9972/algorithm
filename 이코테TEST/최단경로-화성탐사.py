import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

for tc in range(int(input())):
    n = int(input())

    graph = [[INF] * (n+1) for i in range(n+1)]

    costData = []
    for i in range(n):
        costData.append(list(map(int, input().split())))

    q = []
    x, y = 0, 0
    heapq.heappush(q, (costData[x][y], x, y))
    graph[x][y] = costData[x][y]  # 여기 체크 -> 난 graph[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        dist, x, y = heapq.heappop(q)
        if graph[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 이거 체크
                # 여기도 체크  cost = dist + graph[nx][ny] 했었음
                cost = dist + costData[nx][ny]
                if cost < graph[nx][ny]:
                    graph[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(graph[n-1][n-1])

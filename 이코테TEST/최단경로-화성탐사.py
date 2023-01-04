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
    heapq.heappush(q, (costData[0][0], 0, 0))

    while q:
        dist, x, y = heapq.heappop(q)
        if graph[x][y] < dist:
            continue
        for i in graph[x][y]:
            cost = dist + i
            if cost < i:
                i = cost
                heapq.heappush(q, (cost, x, y))

    print(graph[0][0])

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(int(input())):
    n = int(input())

    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    distance = [[INF] * n for i in range(n)]

    x, y = 0, 0
    distance[x][y] = data[x][y]
    q = [(data[x][y], x, y)]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + data[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])

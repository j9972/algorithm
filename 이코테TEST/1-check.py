import sys
from collections import deque
import heapq
input = sys.stdin.readline

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(int(input())):
    n = int(input())

    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    distance = [[INF] * (n+1) for _ in range(n+1)]

    x, y = 0, 0
    q = [(data[x][y], x, y)]
    distance[x][y] = data[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + data[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])

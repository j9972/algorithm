import sys
import heapq
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(int(input())):
    n = int(input())

    INF = int(1e9)

    distance = [[INF] * n for _ in range(n)]

    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))
    
    x,y = 0,0
    distance[x][y] = graph[x][y]
    q = [(graph[x][y], x, y)]

    while q:
        dist, x,y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                cost = dist + graph[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))

    print(distance[n-1][n-1])




                    



        



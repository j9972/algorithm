import sys
input = sys.stdin.readline

n = int(input())
e = int(input())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(e):
    start, end , cost = map(int,input().split())
    # graph[start][end] = cost 을 해줘야하나? 안해도된다봄 이유는 초기화 된 상태니까 무조건 처음에 데이터가 들어온다
    if graph[start][end] > cost:
        graph[start][end] = cost

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j], end=' ')
    print()


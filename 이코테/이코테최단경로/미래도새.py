# 미래도시는 대표적인 플로이드 워셜 문제 ( cuz 양방향 )

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 무한대  값
INF = int(1e9)

# 무한대의 2차원 리스트로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신의 노드부터 자기 자신 노드까지의 거리는 0이다
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선의 거리는 1이다, 문제에서 m+1 줄까지라고 명시했으니 범위는 m이다.
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# k를 들리는것에 대한 최단 거리 구하기
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

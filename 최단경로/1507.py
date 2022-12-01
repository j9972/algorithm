import sys
input = sys.stdin.readline

n = int(input())

INF = int(1e9)

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

road = [[True] * (n+1) for _ in range(n+1)]
res = 0

# for i in range(1, n+1):
#     graph[i][i] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            # a, b, k가 같을 때도 진행을 하면 모두 0이 나온다.
            # -> 자기 자신에서 자기 자신으로 가는 경우는 0이므로 당연히 모든 값이 0이 나온다.
            if k == a or a == b or k == b:
                continue
            # 모두 다른 값(a,b,k) + 다른 도시를 거쳐왔다 ( 도로는 False )
            if graph[a][b] == graph[a][k] + graph[k][b]:
                road[a][b] = False
            # 모두 다른 값 (a,b,k) + 최솟값이 아니다
            elif graph[a][b] > graph[a][k] + graph[k][b]:
                res = -1

# 촤솟값일때
if not res:
    for i in range(n):
        for j in range(i, n):
            # 존재하는 도로의 가중치를 더해줌
            if road[i][j]:
                res += graph[i][j]
print(res)

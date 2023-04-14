# 1389
import sys
input = sys.stdin.readline

INF = int(1e9)
n , e= map(int,input().split())

graph = [[INF] *(n+1) for _ in range(n+1)]

# 양방향
for i in range(e):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신으로 이동은 값이 0 이다
for i in range(1,n+1):
    graph[i][i] = 0

# 최소 거리 구하자
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

res = []
for i in range(1,n+1):
    cnt = 0 # 관계의 수를 더해줄것
    for j in range(1,n+1):  
        cnt += graph[i][j]
    res.append([cnt,i])

res.sort(key=lambda x:(x[0],x[1]))
print(res[0][1])




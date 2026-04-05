import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

graph = [
    [INF] * (n+1)
    for _ in range(n+1)
]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

dic = {}
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if i == j:
            continue
        
        cnt += graph[i][j]
    
    dic[i] = cnt

print(sorted(dic.items(), key=lambda x:(x[1], x[0]))[0][0])


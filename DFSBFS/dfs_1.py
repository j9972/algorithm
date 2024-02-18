n,m = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(m)
]

s,e = [],[]

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in arr:
    s.append(i[0])
    e.append(i[1])

for start, end in zip(s,e):
    graph[start].append(end)
    graph[end].append(start)

cnt = 0

def dfs(v):
    global cnt

    for cur_v in graph[v]:
        if not visited[cur_v]:
            visited[cur_v] = True
            cnt += 1
            dfs(cur_v)

visited[1] = True
dfs(1)
print(cnt)
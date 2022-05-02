import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# graph는 노드 개수의 1개 더 만큼으로 만들어 줘야 한다
n = int(input())
graph = [[] for _ in range(n + 1)]

# 부모 노드
parents = [0 for _ in range(n + 1)]

# 트리 구현
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start, graph, parents):
    for i in graph[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, graph, parents)


dfs(1, graph, parents)

for i in range(2, n+1):
    print(parents[i])

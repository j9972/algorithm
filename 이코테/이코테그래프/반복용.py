import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []
res = 0
last = 0  # 비용이 가장 큰 도로 ( 두개의 도시로 분리하는데 있어서 최소비용을 만들어야 하므로 )

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for e in edges:
    cost, a, b = e
    # 사이클 확인
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
        last = cost

print(res-last)

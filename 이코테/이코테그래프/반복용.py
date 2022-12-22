# 도시분할 -> 신장트리
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

for i in range(1, n+1):
    parent[i] = i

edges = []
res = 0
last = 0  # 가장 큰 비용


for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for e in edges:
    cost, a, b = e
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
        last = cost
print(res-last)

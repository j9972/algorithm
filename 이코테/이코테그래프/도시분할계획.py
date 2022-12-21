# 신장트리 문제
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

edge = []
res = 0
last = 0  # 가장 비용이 큰 간선

for _ in range(m):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()

for e in edge:
    cost, a, b = e
    # 사이클 발생 안하면
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
        last = cost

print(res-last)

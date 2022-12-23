from collections import deque
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

res = 0
edges = []
tot = 0

for i in range(m):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))
edges.sort()

for e in edges:
    cost, x, y = e
    tot += cost
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        res += cost

print(tot - res)

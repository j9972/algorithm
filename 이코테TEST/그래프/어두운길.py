import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []

for _ in range(m):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))

edges.sort()

res = 0
tot = 0
for e in edges:
    cost, a, b = e
    res += cost
    if find(a) != find(b):
        union(a, b)
        tot += cost
print(res-tot)

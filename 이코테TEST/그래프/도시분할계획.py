import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]


def find(x):
    if parent[x] != x:
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

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

last = 0
res = 0
for e in edges:
    cost, a, b = e
    if find(a) != find(b):
        union(a, b)
        res += cost
        last = cost
print(res-last)

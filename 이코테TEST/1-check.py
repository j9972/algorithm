import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    b = find(parent, b)
    a = find(parent, a)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []
edges = []
res = 0

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for e in edges:
    cost, a, b = e
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
print(res)

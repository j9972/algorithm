import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]


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


edge = []

for i in range(m):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()

res = 0
length = 0
for i in edge:
    cost, a, b = i
    if find(a) != find(b):
        union(a, b)
        res += cost
        length = cost
print(res - length)

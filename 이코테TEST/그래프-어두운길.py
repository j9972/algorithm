import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1)


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


# 테이블 나 자신으로 초기화
for i in range(n):
    parent[i] = i

edges = []
res = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
tot = 0

for e in edges:
    cost, a, b = e
    tot += cost
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
print(tot-res)

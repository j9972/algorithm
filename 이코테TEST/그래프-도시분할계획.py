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
for i in range(1, n+1):
    parent[i] = i

edges = []
res = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

last = 0
for e in edges:
    cost, a, b = e
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
        last = cost  # last인 이유는 edges가 정렬이 되었기에 가장 마지막에 나오는 cost가 가장 큰 비용
print(res - last)

# 신장트리
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
edge = []
parent = [0] * (n+1)
res = 0

for i in range(1, n+1):  # 부모테이블 자기 자신으로 초기화시 범위 조심
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()  # 비용순으로 정렬
tot = 0

for e in edge:  # 간선을 1개씩 확인
    cost, a, b = e
    tot += cost
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost

print(tot-res)

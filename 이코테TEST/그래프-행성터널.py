import sys
input = sys.stdin.readline

n = int(input())
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

x = []
y = []
z = []

edges = []
res = 0

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))  # 지점, 노드 번호넣기
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

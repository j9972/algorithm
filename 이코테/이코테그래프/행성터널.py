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


n = int(input())
parent = [0] * (n+1)
edges = []
res = 0

for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))  # 그 지점 또한 넣어준다
    y.append((data[1], i))
    z.append((data[2], i))
x.sort()
y.sort()
z.sort()

# x[i+1][0]-x[i][0] = cost
# a ( 출발지점 ) = x[i][1]
# b ( 도착지점 ) = x[i+1[1]
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for e in edges:  # 간선을 1개씩 확인
    cost, a, b = e
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost

print(res)

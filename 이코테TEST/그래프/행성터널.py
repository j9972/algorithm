import sys
input = sys.stdin.readline

edges = []
x = []
y = []
z = []

n = int(input())  # 터널 개수 : N-1
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


for i in range(1, n+1):
    a, b, c = map(int, input().split())
    x.append((a, i))  # 인덱스 번호까지 같이 넣음
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((abs(x[i+1][0] - x[i][0]), x[i][1], x[i+1][1]))
    edges.append((abs(y[i+1][0] - y[i][0]), y[i][1], y[i+1][1]))
    edges.append((abs(z[i+1][0] - z[i][0]), z[i][1], z[i+1][1]))

edges.sort()

res = 0
for e in edges:
    cost, a, b = e
    if find(a) != find(b):
        union(a, b)
        res += cost
print(res)

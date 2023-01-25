import sys
input = sys.stdin.readline

n, m = map(int, input().split())


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


parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            union(parent, i+1, j+1)

info = list(map(int, input().split()))

for i in range(m-1):
    if find(parent, info[i]) != find(parent, info[i+1]):
        print('NO')
    else:
        print('YES')
    break

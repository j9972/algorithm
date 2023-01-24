import sys
input = sys.stdin.readline

n, m = map(int, input().split())


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


parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

info = list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] == 1:

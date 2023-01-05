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


for i in range(1, n+1):
    parent[i] = i


for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 0:
            union(parent, i+1, j+1)

plan = list(map(int, input().split()))

res = False
for i in range(m-1):
    if find(parent, plan[i]) == find(parent, plan[i+1]):
        res = True

if res:
    print('YES')
else:
    print('NO')

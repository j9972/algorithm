# 서로소 집합  알고리즘
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:  # 한줄씩 받고 그 줄마다 행열값을 주니까 data[i][j] 라고 하면 안된다
            union(parent, i+1, j+1)

d = list(map(int, input().split()))

res = True
for i in range(m-1):
    if find_parent(parent, d[i]) != find_parent(parent, d[i+1]):
        res = False

if res:
    print('YES')
else:
    print('NO')

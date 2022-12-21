# 서로소 집합 문제
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [0] * (n+1)


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


for i in range(0, n+1):
    data[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union(data, a, b)
    elif oper == 1:
        if find_parent(data, a) == find_parent(data, b):
            print('YES')
        else:
            print('NO')

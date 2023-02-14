# 서로소 문제
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

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


data = []
for i in range(n):
    data.append(list(map(int, input().split())))

info = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            union(i+1, j+1)


for i in range(m-1):
    if find(info[i]) == find(info[i+1]):
        print('YES')
    else:
        print('NO')
    break

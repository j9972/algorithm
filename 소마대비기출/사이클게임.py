# 골드4 - 사이클 게임
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n)]


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


cnt = 0
data = []
for i in range(m):
    a, b = map(int, input().split())
    data.append([a, b])

for i in range(m):
    if find(data[i][0]) != find(data[i][1]):
        union(data[i][0], data[i][1])
        cnt += 1
    else:
        break

if cnt == m:
    print(0)
else:
    print(cnt+1)

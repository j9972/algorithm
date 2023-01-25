import sys
input = sys.stdin.readline


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


g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i
cnt = 0
for i in range(p):
    data = find(parent, int(input()))
    if data == 0:
        break
    union(parent, data, data-1)
    cnt += 1

print(cnt)

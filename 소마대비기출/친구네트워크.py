import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        num[a] += num[b]
    print(num[a])


for tc in range(int(input())):
    n = int(input())
    parent, num = {}, {}
    for i in range(n):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] = 1

        union(a, b)

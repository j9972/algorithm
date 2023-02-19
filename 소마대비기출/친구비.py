# 골드 4 - 16562
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

cost = list(map(int,input().split()))

edges = []

parent = {}
num = {}

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        num[a] += num[b]
    print(num[a])

for i in range(m):
    a,b = map(int,input().split())
    if a not in parent:
        parent[a] = a
        num[a] = cost[a-1]
    if b not in parent:
        parent[b] = b
        num[b] = cost[b-1]
    union(a,b)


import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
cost = [0] + list(map(int,input().split()))

parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[a] = b
    cost[b] = min(cost[a],cost[b])

for i in range(m):
    a,b = map(int,input().split())
    union(a,b)

res = 0
for i in range(1,n+1):
    if parent[i] == i:
        res += cost[i]
if res > k:
    print('Oh no')
else:
    print(res)
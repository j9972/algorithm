import sys
input = sys.stdin.readline

n,m = map(int,input().split())

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

def find(parent,x):
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

for i in range(m):
    value, a,b = map(int,input().split())
    if value == 0:
        union(parent, a,b)
    elif value == 1:
        if find(parent,a) != find(parent,b):
            print('NO')
        else:
            print('YES')

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

board = []
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j] == 1:
            union(parent,i+1,j+1)


data = list(map(int,input().split()))

res = True
for i in range(m-1):
    if find(parent, data[i]) != find(parent, data[i+1]):
        res = False

if res:
    print('YES')
else:
    print('NO')
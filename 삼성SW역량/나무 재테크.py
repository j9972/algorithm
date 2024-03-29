import sys
from collections import deque

input = sys.stdin.readline

n,m,k = map(int,input().split())

dxs, dys = [-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]

# 겨울마다 주는 양분
extra_feed = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 트리
tree = [
    [deque() for _ in range(n)]
    for _ in range(n)
]

# 기본 양분
feed = [
    [5 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x,y,age = map(int,input().split())
    tree[x-1][y-1].append(age)

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def ss():
    for i in range(n):
        for j in range(n):
            dead = 0
            new_tree = deque()
            for age in tree[i][j]:

                if feed[i][j] >= age:
                    feed[i][j] -= age
                    new_tree.append(age+1)
                else:
                    dead += age // 2
            
            feed[i][j] += dead
            tree[i][j] = new_tree

def fw():
    tmp_tree = []
    for x in range(n):
        for y in range(n):
            for age in tree[x][y]:
                if age % 5 == 0:
                    for dx, dy in zip(dxs, dys):
                        nx,ny = x + dx, y + dy

                        if not in_range(nx,ny):
                            continue

                        tmp_tree.append((nx,ny))
                else:
                    continue
            feed[x][y]  += extra_feed[x][y]
            
    for pos in tmp_tree:
        x,y = pos
        tree[x][y].appendleft(1)

ans = 0
def count_tree():
    global ans

    for i in range(n):
        for j in range(n):
            ans += len(tree[i][j])

for _ in range(k):
    ss()
    fw()

count_tree()
print(ans)        
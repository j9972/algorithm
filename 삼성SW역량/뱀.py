import sys
from collections import deque

n = int(input())
k = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs,dys = [0,1,0,-1], [1,0,-1,0]

for _ in range(k):
    x,y = map(int,input().split())
    arr[x-1][y-1] = 1

l = int(input())

direct = []
for i in range(l):
    x,c = input().split()
    direct.append((int(x), c))

def turing(d, direction):
    if d == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(nx,ny):
    return in_range(nx,ny) and arr[nx][ny] != 2

x,y = 0,0
q = [(x,y)]
arr[x][y] = 2

def bfs():
    global x,y,q
    time, idx, cur_d = 0,0,0

    while True:
        nx,ny = x + dxs[cur_d], y + dys[cur_d]

        if can_go(nx,ny):
            if arr[nx][ny] == 0:
                hx,hy = q.pop(0)
                arr[hx][hy] = 0

            q.append((nx,ny))
            arr[nx][ny] = 2
        else:
            time += 1
            break
                
        time += 1
        x,y = nx,ny

        if idx < l and time == direct[idx][0]:
            cur_d = turing(direct[idx][1], cur_d)
            idx += 1
            
    return time

print(bfs())

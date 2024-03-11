import sys

n,m,x,y,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

order = list(map(int,input().split())) # 차후에 1씩 빼기

dxs,dys = [0,0,-1,1], [1,-1,0,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

dice = [0,0,0,0,0,0]

def turn(i):
    # 회전 순서랑 매치 시키면서 전개도를 그리면 된다
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

    if i == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif i == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif i == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    
for i in order:
    nx,ny = x + dxs[i-1], y + dys[i-1]

    if not in_range(nx,ny):
        continue
    
    turn(i)

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[-1]
    else:
        dice[-1] = arr[nx][ny]
        arr[nx][ny] = 0
    
    x,y = nx,ny
    
    print(dice[0])
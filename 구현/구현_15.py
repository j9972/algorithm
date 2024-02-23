# 주사위 
n,m,x,y = map(int,input().split())

x -= 1
y -= 1

direction = list(input().split())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

arr[x][y] = 6

# 동서남북
dx,dy = [0,0,1,-1], [1,-1,0,0]

move_dir = {
    'R' : 0,
    'L' : 1,
    'D' : 2,
    'U' : 3   
}

U,F,R = 1,2,3

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def simulate(direct):
    global x,y,U,F,R

    nx,ny = x + dx[direct] , y + dy[direct]

    if not in_range(nx,ny):
        return

    x,y = nx,ny

    if direct == 0:
        U,F,R = 7-R,F,U
    elif direct == 1:
        U,F,R = R,F,7-U
    elif direct == 2:
        U,F,R = 7-F,U,R
    elif direct == 3:
        U,F,R = F,7-U,R
    
    arr[x][y] = 7 - U

for d in direction:
    simulate(move_dir[d])

val = 0
for i in range(n):
    for j in range(n):
        val += arr[i][j]
print(val)
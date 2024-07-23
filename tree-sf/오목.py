arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

def in_range(x,y):
    return 0<=x<19 and 0<=y<19

dxs,dys = [0,1,1,1], [1,0,1,-1]

def check(x,y):
    global flag
    for dx, dy in zip(dxs,dys):
        flag = True

        for i in range(1,5):
            if not in_range(x + dx * i, y + dy * i) or arr[x][y] != arr[x + dx * i][y + dy * i]:
                flag = False
                break
        
        if flag:
            print(arr[x][y])
            print(x+1+dx*2, y+1+dy*2)
            return

flag = False
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0 and not flag:
            check(i,j)

if not flag:
    print(0)
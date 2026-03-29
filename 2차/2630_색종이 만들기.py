import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

w, b = 0,0

def possible(x,y,size):
    color = arr[x][y]

    for i in range(x,x+size):
        for j in range(y,y+size):
            if color != arr[i][j]:
                return False
    return True

def dfs(x,y,size):
    global w,b

    if size == 1:
        if arr[x][y] == 1:
            b += 1
        else:
            w += 1
        return 

    if possible(x,y,size):
        if arr[x][y] == 1:
            b += 1
        else:
            w += 1
        return

    half = size // 2

    dfs(x,y,half)
    dfs(x+half,y,half)
    dfs(x,y+half,half)
    dfs(x+half,y+half,half)

dfs(0,0,n)
print(w)
print(b)

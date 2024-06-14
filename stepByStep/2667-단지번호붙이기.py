n = int(input())

arr = [
    list(map(int,input()))
    for _ in range(n)
]

size_home = []
size = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global size

    if in_range(x,y) and arr[x][y] == 1:
        arr[x][y] = 0
        size += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            size_home.append(size)
            size = 0

length = len(size_home)
print(length)
for i in sorted(size_home):
    print(i)
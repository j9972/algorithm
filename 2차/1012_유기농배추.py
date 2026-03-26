import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for _ in range(int(input())):

    n,m,k = map(int,input().split())
    cnt = 0
    
    field = [
        [0] * m
        for _ in range(n)
    ]

    def in_range(x,y):
        return 0<=x<n and 0<=y<m

    def dfs(x,y):
        if in_range(x,y) and field[x][y] == 1:
            field[x][y] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
        return False

    for _ in range(k):
        x,y = map(int,input().split())
        field[x][y] = 1

    for x in range(n):
        for y in range(m):
            if dfs(x,y):
                cnt += 1
    
    print(cnt)
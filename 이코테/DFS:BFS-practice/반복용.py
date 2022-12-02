import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().strip())))


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if data[x][y] == 0:
            data[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False


res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res += 1
print(res)

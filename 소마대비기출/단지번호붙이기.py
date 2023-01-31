# 실버 1 - 2667
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().rstrip())))

visited = [[False] * (n+1) for _ in range(n+1)]
res = []
ans = 0


def dfs(x, y):
    global ans
    if 0 <= x < n and 0 <= y < n and data[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        ans += 1
        data[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            res.append(ans)
            ans = 0

res.sort()
print(len(res))
for i in res:
    print(i)

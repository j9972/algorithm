# 실버 1 - 2667
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().strip())))

ans = 0


def dfs(x, y):
    global ans
    if 0 <= x < n and 0 <= y < n and data[x][y] != 0:
        ans += 1
        data[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


res = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            res.append(ans)
            ans = 0
res.sort()
print(len(res))
for i in res:
    print(i)

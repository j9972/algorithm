# 사다리
import sys
input = sys.stdin.readline

data = []

n, m, h = map(int, input().split())

ans = 4

visited = [[False] * (n+1) for _ in range(h+1)]

for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

for i in range(1, h+1):
    for j in range(1, n):
        if not visited[i][j] and not visited[i][j+1] and not visited[i][j-1]:
            data.append([i, j])


def check():
    for i in range(1, n+1):
        now = i

        for j in range(1, h+1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1

        if now != i:
            return False
    return True


def dfs(cnt, idx):
    global ans

    if cnt >= ans:
        return
    if check():
        ans = cnt
        return

    for c in range(idx, len(data)):
        x, y = data[c]

        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(cnt+1, c+1)
            visited[x][y] = False


dfs(0, 0)
print(ans if ans < 4 else -1)

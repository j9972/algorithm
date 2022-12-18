import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

visited = [[False] * (n+1) for _ in range(h+1)]

sadari = []
for i in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

ans = 4

for i in range(1, h+1):
    for j in range(1, n):
        if not visited[i][j] and not visited[i][j-1] and not visited[i][j+1]:
            sadari.append([i, j])


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

    if m == 0:
        print(0)
        exit(0)

    if cnt >= ans:
        return
    if check():
        ans = cnt
        return

    for c in range(idx, len(sadari)):
        x, y = sadari[c]

        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(cnt+1, c+1)
            visited[x][y] = False


dfs(0, 0)

print(ans if ans < 4 else -1)

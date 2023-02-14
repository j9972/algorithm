import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = [[0]*(m+1) for _ in range(n+1)]
data = []
for i in range(n):
    data.append(list(map(int, input().split())))


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:  # 0인가 2인가?
                graph[nx][ny] = 2
                virus(nx, ny)


def score():
    score = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score += 1
    return score


res = 0


def dfs(count):
    global res
    if count == 3:
        for i in range(n):
            for j in range(m):
                graph[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    virus(i, j)
        res = max(res, score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(res)

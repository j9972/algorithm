n, m = map(int, input().split())

data = []
graph = [[0] * m for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny < m and ny >= 0:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                virus(nx, ny)


def getScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score += 1
    return score


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
        res = max(res, getScore())
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

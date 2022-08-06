# 농장관리
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

visited = [[False]*(m+1) for _ in range(n+1)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def dfs(x, y):
    global mountainHeight

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        # 주의점 : nx ny 는 현재 x y를 기준으로 주변 산봉우리 그래서 nxny가 더 크면 산봉우리의 조건에 맞지 않다
        if 0 <= nx < n and 0 <= ny < m:
            if board[x][y] < board[nx][ny]:
                mountainHeight = False
            if visited[nx][ny] == False and board[x][y] == board[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)


res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] > 0 and not visited[i][j]:
            mountainHeight = True
            dfs(i, j)
            if mountainHeight:
                res += 1
print(res)

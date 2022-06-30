t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                dfs(nx, ny)


for i in range(t):
    count = 0
    m, n, k = map(int, input().split())  # m = 가로, n = 세로 , k = 배추 개수
    board = [[0] * m for _ in range(n)]  # 0으로 일단 만들어 놓은 배열 상태

    for j in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    for a in range(n):
        for b in range(m):
            if board[b][a] == 1:
                dfs(x, y)
                count += 1
    print(count)

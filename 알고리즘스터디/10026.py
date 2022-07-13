# dfs - 적록색명 - done
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rgb = 0
gb = 0

board = []
for i in range(n):
    board.append(list(input()))

visited = [[False] * (n+1) for _ in range(n+1)]

# dfs의 핵심은 방문 처리와 재귀함수의 실행이다.


def dfs(x, y):
    visited[x][y] = True
    color = board[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            if color == board[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            rgb += 1
            dfs(i, j)

board_new = [] 
# 적록색맹인 경우를 확인해서 board랑 visited를 초기화 시키기
for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'

visited = [[False] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            gb += 1
            dfs(i, j)

print(rgb, gb)

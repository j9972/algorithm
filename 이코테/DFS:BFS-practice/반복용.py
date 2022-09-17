n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input())))


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if board[x][y] == 0:
            board[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False


check = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            check += 1
print(check)

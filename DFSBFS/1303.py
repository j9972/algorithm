# 전쟁 - 전투 -> Dfs

n, m = map(int, input().split())

board = []
boardW = []
boardB = []

for i in range(n):
    board.append(list(map(str, input())))
    for j in range(m):
        if board[i][j] == 'W':
            boardW[i][j] = board[i][j]
        elif board[i][j] == 'B':
            boardB[i][j] = board[i][j]


count = []
num = 0


def dfs(x, y):
    global num
    if 0 <= x < n and 0 <= y < n and boardB[x][y]:
        board[x][y] = 'S'
        num += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


def dfsW(x, y):
    global numW
    if 0 <= x < n and 0 <= y < n and board[x][y] == 'W':
        board[x][y] = 'S'
        numW += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count.append(numB**2)
            numB = 0
        if dfsW(i, j) == True:
            count.append(numW**2)
            numW = 0


for i in range(len(count)):
    print(count[i])

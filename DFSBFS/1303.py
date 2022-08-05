# 전쟁 - 전투 -> Dfs
m, n = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(str, input())))

wCount = 0
wTotal = 0

bCount = 0
bTotal = 0


def dfs(x, y):
    global wCount

    if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
        board[x][y] = 'S'
        wCount += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


def dfsS(x, y):
    global bCount

    if 0 <= x < n and 0 <= y < m and board[x][y] == 'B':
        board[x][y] = 'S'
        bCount += 1
        dfsS(x-1, y)
        dfsS(x+1, y)
        dfsS(x, y-1)
        dfsS(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            wTotal += wCount ** 2
            wCount = 0

for i in range(n):
    for j in range(m):
        if dfsS(i, j) == True:
            bTotal += bCount ** 2
            bCount = 0


print(wTotal, bTotal)

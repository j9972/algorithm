import sys
sys.setrecursionlimit(10**9)

# 세로가 m
m, n, k = map(int, input().split())

board = [[0]*(n+1) for _ in range(m+1)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if board[i][j] == 0:
                board[i][j] = 1

num = 0
count = []


def dfs(x, y):
    global num
    if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
        board[x][y] = 1
        num += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


res = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j) == True:
            res += 1
            count.append(num)
            num = 0

count.sort()

print(res)
for i in count:
    print(i, end=' ')

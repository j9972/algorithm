import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

data = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                virus(nx, ny)


def getScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global res
    if count == 3:
        for i in range(n):
            for j in range(m):
                data[i][j] = board[i][j]
        for i in range(n):
            for j in range(m):
                if data[i][j] == 2:
                    virus(i, j)
        res = max(res, getScore())
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1
                dfs(count)
                board[i][j] = 0
                count -= 1


dfs(0)
print(res)

# import sys
# import copy
# from collections import deque

# input = sys.stdin.readline

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# q = deque()

# def bfs():
#     global ans
#     w = copy.deepcopy(arr)
#     for i in range(N):
#         for j in range(M):
#             if w[i][j]==2:
#                 q.append([i,j])

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if w[nx][ny]==0:
#                     w[nx][ny] = 2
#                     q.append([nx,ny])
#     cnt = 0
#     for i in w:
#         cnt+=i.count(0)
#     ans = max(ans,cnt)

# def wall(x):
#     if x==3:
#         bfs()
#         return
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j]==0:
#                 arr[i][j]=1
#                 wall(x+1)
#                 arr[i][j]=0

# wall(0)
# print(ans)

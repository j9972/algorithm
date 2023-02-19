# 골드3 - 1520
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

d = [[0] * m for _ in range(n)]
d[0][0] = 1

def dfs(x,y):
    for x in range(n):
        for y in range(m):
            if x == n-1 and y == m-1:
                return d[x][y]

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0<=nx<n and 0<=ny<m:
                    if data[nx][ny] < data[x][y]:
                        d[nx][ny] += d[x][y]
    return d[x][y]

# def dfs(x,y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0<=nx<n and 0<=ny<m:
#             if nx == n-1 and ny == m-1:
#                 return d[nx][ny]
#             else:
#                 if data[nx][ny] < data[x][y]:
#                     d[nx][ny] += d[x][y]
#     return d[n-1][m-1]

print(dfs(0,0))
    



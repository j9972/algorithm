# dfs 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# 런타임 에러때문에 써줘야함

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                # 여기서 graph[nx][ny]이 값을 0이하로 바꿔줘야함
                # 맨 아래 for 문에서 graph[i][j] 가 0이 아닐때 count 를 증가하므로
                graph[nx][ny] = 0
                dfs(nx, ny)


for i in range(t):
    m, n, k = map(int, input().split())
    count = 0
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        # x의 범위가 0 부터 m-1까지 이므로 2번째에 오는게 맞다 ( 같은 원리로 y는 첫번째 )
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                count += 1
                dfs(i, j)

print(count)

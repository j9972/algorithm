# 안전 영역 체크 -> dfs : 음료수 얼려먹기 같음
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

# graph는 입력값이 주어지는 2차원배열
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

count = 1


def dfs(x, y, h):
    if 0 <= x < n and 0 <= y < n and graph[x][y] >= h and not visited[x][y]:
        visited[x][y] = True
        dfs(x-1, y, h)
        dfs(x+1, y, h)
        dfs(x, y-1, h)
        dfs(x, y+1, h)
        return True
    return False


for h in range(1, 101):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= h and not visited[i][j] and dfs(i, j, h) == True:
                cnt += 1
                visited[i][j] = True

    count = max(count, cnt)


print(count)

# dfs문제
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dx = [1, 1, -1, -1, 1, -1, 0, 0]
# dy = [0, 1, 0, 1, -1, -1, 1, -1]


# def dfs(x, y):
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         # h랑 w 잘 생각해서 하기
#         if 0 <= nx < h and 0 <= ny < w:
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 dfs(nx, ny)

def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y+1)
            dfs(x-1, y)
            dfs(x-1, y-1)
            dfs(x+1, y+1)
            dfs(x+1, y)
            dfs(x+1, y-1)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False


# 특정 수가 나올때까지 계속 이어질라면 특정 조건에서 끝나는 조건을 만들어줘야 하늗네 그것은 while
# 문으로 만들고 while문 안에서 입력값 및 그래프 만들어줘야한다.
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    res = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                res += 1
    print(res)

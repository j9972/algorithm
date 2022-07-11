# # dfs 문제
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
# # 런타임 에러때문에 써줘야함

# t = int(input())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def dfs(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[nx][ny] == 1:
#                 # 여기서 graph[nx][ny]이 값을 0이하로 바꿔줘야함
#                 # 맨 아래 for 문에서 graph[i][j] 가 0이 아닐때 count 를 증가하므로
#                 graph[nx][ny] = 0
#                 dfs(nx, ny)


# for i in range(t):
#     m, n, k = map(int, input().split())
#     count = 0
#     리프리헨션 쓸때 가로 세로 체크 제대로 하기 -> 가로 세로 순서
#     graph = [[0]*m for _ in range(n)]

#     for _ in range(k):
#         x, y = map(int, input().split())
#         x,y는 위치 값 ( 2차원 배열속의 위치 값인데, x는 세로 y는 가로이기 때문에 y x 순서)
#         graph[y][x] = 1

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] != 0:
#                 count += 1
#                 # 함수를 재귀적으로 호출, 다른 방법으로는 이코테에 음료수 얼려먹기 방법도 있다
#                 dfs(i, j)

#     # print(count) 이거 선언하는 위치 조심하기
#     print(count)
import sys
sys.setrecursionlimit
input = sys.stdin.readline

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                dfs(nx, ny)


for i in range(t):
    m, n, k = map(int, input().split())
    # 컴프리 헨션은 가로 세로 순서로 해야함을 잊지말자
    board = [[0] * m for _ in range(n)]

    # 지렁이의 갯수
    count = 0

    for i in range(k):
        # x,y는 배추의 위치를 의미한다. 근데 범위가 x는 m-1 -> m이 가로를 의미!!
        x, y = map(int, input().split())
        # 여기서 x는 가로를 의미, y는 세로를 의미 ( 가로의미는 2번째 인덱스를 의미 )
        board[y][x] = 1

    for i in range(n):
        for j in range(m):
            # dfs 함수가 0일때는 배추가 없어서 재귀함수를 일으키지 못하므로
            if board[i][j] != 0:
                count += 1
                dfs(i, j)

    print(count)

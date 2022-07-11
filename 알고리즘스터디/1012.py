# Dfs
# 빠른 입력을 위한 import 선언
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# testcase number
t = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 배추가 2차원 배열을 넘어가지 않는 범위 내에서 있다면 재귀적으로 호출
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1:
                # 그 위치의 값을 변경하지 않으면, 무한 호출
                board[nx][ny] = 0
                dfs(nx, ny)


for i in range(t):
    m, n, k = map(int, input().split())
    # 지렁이 수를 카운트 하기 위함
    count = 0

    # 기본적인 배열로써 값을 지정
    # 리프리헨션 쓸때 가로 세로 체크 제대로 하기 -> 가로 세로 순서
    board = [[0] * m for _ in range(n)]

    for i in range(k):
        # x의 범위가 m-1까지 이므로, 2차원 배열의 인덱스 순서가 저렇게 되는 것이 맞다
        x, y = map(int, input().split())
        board[y][x] = 1

    for i in range(n):
        for j in range(m):
            # 배추가 있다면 함수 호출
            if board[i][j] == 1:
                count += 1
                dfs(i, j)
    print(count)

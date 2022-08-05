# 농장관리
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

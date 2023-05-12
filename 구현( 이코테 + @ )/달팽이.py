# 1913 실버 3
import sys
input = sys.stdin.readline

n = int(input())
point = int(input())

board = [[0] * n for _ in range(n)]

# 시작 번호
num = 2
size = 3

# 중앙 위치
x=n//2
y=n//2

board[x][y] = 1

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while (x != 0 or y != 0):
    while (num <= size * size):
        if (x == y == (n//2)):
            up, right, down, left = size, size-2, size-1, size-1
            x += dx[0]
            y += dy[0]
            up -= 1

        elif (right > 0):
            x += dx[3]
            y += dy[3]
            right -= 1
        elif (down > 0):
            x += dx[1]
            y += dy[1]
            down -= 1
        elif (left > 0):
            x += dx[2]
            y += dy[2]
            left -= 1
        else:
            x += dx[0]
            y += dy[0]
            up -= 1

        board[x][y] = num
        num += 1
    
    size += 2
    n -= 2

find_x , find_y = 0,0

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == point:
            find_x , find_y = i+1,j+1
        print(board[i][j], end=' ')
    print('')
print(find_x, find_y)

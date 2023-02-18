# 골드5 - 2174
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n,m = map(int,input().split())

robot = dict()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0,-1]

board = [[0] * a for _ in range(b)]

direction = []
for i in range(1,n+1):
    x,y,d = input().split()
    if d == 'N':
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    elif d == 'W':
        d = 3

    board[(b-int(y))][int(x)-1] = 1
    robot[i] = [(b-int(y)),int(x)-1,d]

command = []
for i in range(m):
    x,y,z = input().split()
    command.append([int(x),y,int(z)])

for row,col,repeat in command:
    for _ in range(repeat):
        if col == 'F':
            curx,cury,direct = robot[row]
            next_x = curx + dx[direct]
            next_y = cury + dy[direct]

            if not (0<=next_x<b and 0<=next_y<a):
                print('Robot {} crashes into the wall'.format(i))
                exit()

            elif board[next_x][next_y] == 1:
                for i in robot:
                    if next_x == robot[i][0] and next_y == robot[i][1]:
                        print('Robot {} crashes into robot {}'.format(row,i))
                        exit()
            else:
                board[curx][cury] = 0
                board[next_x][next_y] = 1
                robot[row][0] = next_x
                robot[row][1] = next_y


        elif col == 'R':
            robot[row][2] = (robot[row][2] + 1) % 4
        else:
            robot[row][2] = (robot[row][2] - 1) % 4
print("OK")

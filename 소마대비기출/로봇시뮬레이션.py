# 골드5 - 2174
import sys
input = sys.stdin.readline
from collections import deque

a,b = map(int,input().split())
n,m = map(int,input().split())

e,n,w,s = 0,1,2,3
dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = []
for i in range(b):
    for j in range(a):
        board.append(list(map(int,input().split())))

init = []
for i in range(n):
    x,y,direction= map(str,input().split())
    init.append([int(x),int(y),direction, i+1]) # i는 로봇 종류  (1~N번 순서)

move= []
for i in range(m):
    robot_type, order, repeat_time = map(str,input().split())
    move.append([int(robot_type), order, int(repeat_time)])

def bfs():
    q = deque()
    x,y = init[0][0], init[0][1]

    q.append((x,y))

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        for i in range(m):
            if move[i][1] == 'F':
                
                
            elif move[i][1] == 'L':
                pass
            elif move[i][1] == 'R':
                pass


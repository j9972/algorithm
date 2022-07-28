import sys
input = sys.stdin.readline

n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

board.sort(key=lambda x: (x[1], x[0]))

for i in board:
    print(i[0], i[1])

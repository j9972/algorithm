import sys
input = sys.stdin.readline

n = int(input())

board = []
for i in range(n):
    data = input().split()
    board.append((int(data[0]), data[1]))

board.sort(key=lambda x: x[0])


for i in board:
    print(i[0], i[1])

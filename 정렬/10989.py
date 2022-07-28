import sys
input = sys.stdin.readline

n = int(input())

board = [0] * 10001
for i in range(n):
    data = int(input())
    board[data] = board[data] + 1

for i in range(10001):
    if board[i] != 0:
        for _ in range(board[i]):
            print(i)

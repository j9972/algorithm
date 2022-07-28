# 국영수 문제
import sys
input = sys.stdin.readline

n = int(input())

board = []
for i in range(n):
    data = list(input().split())
    board.append((data[0], int(data[1]), int(data[2]), int(data[3])))

board.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in board:
    print(i[0])

# 1051 숫자 정사각형
import sys
input = sys.stdin.readline

n, m = map(int, input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
v = []
for i in range(n):
    board = list(map(int, input().split()))
    v.append(min(board))
print(max(v))

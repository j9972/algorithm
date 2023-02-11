import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

t, w = map(int, input().split())
d = [[0] * w for _ in range(t)]

for i in range(t):
    data = int(input())
    d[i][data-1] = 1

for i in range(t):

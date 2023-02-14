# 실버 1 - 2302
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
d = [0 for _ in range(1, n+1)]

for i in range(m):
    data = int(input())
    d[data-1] = 1

# print(d) -> [0,0,0,1,0,0,1,0,0]

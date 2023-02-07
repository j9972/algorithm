# 다시 부분
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            leftup = 0
        else:
            leftup = d[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = d[i-1][j]

        d[i][j] += max(leftup, up)
print(max(d[n-1]))

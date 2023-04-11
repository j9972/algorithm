# 1149
import sys
input = sys.stdin.readline

n = int(input())

d = []
for i in range(n):
    red, green, blue = map(int,input().split())
    d.append([red, green, blue])

for i in range(1,n):
    for j in range(3):
        if j == 0:
            d[i][j] += min(d[i-1][j+1],d[i-1][j+2])
        elif j == 1:
            d[i][j] += min(d[i-1][j+1],d[i-1][j-1])
        elif j == 2:
            d[i][j] += min(d[i-1][j-2],d[i-1][j-1])

res = 10**9
for i in range(3):
    if res > d[n-1][i]:
        res = d[n-1][i]
print(res)

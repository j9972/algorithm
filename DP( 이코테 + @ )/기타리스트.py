# 1495
import sys
input = sys.stdin.readline

n,start,m = map(int,input().split())
vol = list(map(int,input().split()))

d = [[False] * (m+1) for _ in range(n+1)]
d[0][start] = True

for i in range(n):
    for j in range(m+1):
        if d[i][j] == True:
            #print(j-vol[i],j+vol[i])
            for next in [j-vol[i] , j+vol[i]]:
                if 0<=next<=m:
                    d[i+1][next] = True

res = -1
for i in range(m,-1,-1):
    if d[n][i] == True:
        res = i
        break
print(res)
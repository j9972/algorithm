# 골드5 - 12865
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
product = [[0,0]]
for i in range(n):
    w,v = map(int,input().split())
    product.append((w,v))

d = [[0] * (1+k) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = product[i]
        if j >= w: # 감당가능
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)
        else:
            d[i][j] = d[i-1][j]
print(max(d[n]))
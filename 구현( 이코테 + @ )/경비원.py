# 2564 실버 1
import sys
input = sys.stdin.readline

m,n = map(int,input().split())

def distance(x,y):
    if x == 1:
        return y
    if x == 2:
        return 2*m+n-y
    if x == 3:
        return 2*(m+n) - y
    if x == 4:
        return m+y

res = []
for i in range(int(input())+1):
    x,y = map(int,input().split())
    res.append(distance(x,y))

#print(res)
cnt = 0
for i in range(len(res)-1):
    dist = abs(res[-1] - res[i])
    cnt += min(dist, 2*(n+m)-dist)

print(cnt)
# 1449 실버3
import sys
input = sys.stdin.readline

n,l = map(int,input().split())
points = list(map(int,input().split()))
points.sort()

cnt = 1
dist = 0
for i in range(1,n):
    dist += points[i] - points[i-1]
    if l > dist:
        continue
    else:
        cnt += 1
        dist = 0
print(cnt)
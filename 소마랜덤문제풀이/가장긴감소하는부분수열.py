# 실버 3 11722
import sys
input = sys.stdin.readline

n = int(input())
d = [1] * n
data = list(map(int,input().split))

for i in range(1,n):
    for j in range(i):
        if data[i] < data[j]:
            d[i] = max(d[i],d[j]+1)
print(max(d))

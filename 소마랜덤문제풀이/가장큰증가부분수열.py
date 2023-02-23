# 실버2 - 11055
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

d = [1] * n
d[0] = data[0]
for i in range(1,n):
    for j in range(i):
        if data[i] > data[j]:
            d[i] = max(d[i], d[j] + data[i])
print(max(d))
# LIS 뒤집은 문제
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

data.reverse()

d = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if data[i] > data[j]:
            d[i] = max(d[j]+1, d[i])

print(n-max(d))
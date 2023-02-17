# 실버1 - 2156
import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 100000

data = [0] * 10000
for i in range(n):
    data[i] = int(input())

d[0] = data[0]
d[1] = data[0] + data[1]
d[2] = max(data[0]+data[2], data[1]+data[2], d[1])

for i in range(3, n):
    d[i] = max(d[i-3]+data[i-1]+data[i], d[i-2]+data[i], d[i-1])

print(max(d))

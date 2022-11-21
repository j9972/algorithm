# 바닥 공사
import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 1000

d[1] = 1
d[2] = 3

for i in range(3, n):
    d[i] = ((d[i-2]*2) + d[i-1]) % 796796

print(d[n])

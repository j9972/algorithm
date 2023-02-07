# 다시 부분
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d = [0] * 1001

d[0] = 0
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 10007

print(d[n])

# 실버3 - 2193
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)
d[0] = 1
d[1] = 1

for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n-1])
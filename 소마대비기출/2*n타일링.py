# 실버 3 - 11726
import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)

d = [0] * (n+1)
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 5

for i in range(5, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n] % 10007)

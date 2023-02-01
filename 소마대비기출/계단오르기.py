# 실버3-> 2579
import sys
input = sys.stdin.readline

n = int(input())
stair = [0]
for i in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[1])
else:
    d = [0] * 301
    d[0] = 0
    d[1] = stair[1]
    d[2] = stair[1] + stair[2]
    for i in range(3, n+1):
        d[i] = max(d[i-3] + stair[i-1], d[i-2]) + stair[i]

    print(d[n])

# 실버1 - 1697
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = [0] * 100001
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if n <= k:
        d[i] = min(d[i], d[i*2]+1)
    else:
        d[i] = min(d[i], d[i-1])

print(d[n])

# 실버 2 - 1182
from itertools import combinations as cb
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0

for i in range(1, n+1):
    info = list(cb(data, i))
    for j in info:
        if sum(j) == s:
            cnt += 1
print(cnt)

# 골드 5 - 1038
from itertools import combinations as cb
import sys
input = sys.stdin.readline

n = int(input())
res = []
nums = [i for i in range(10)]

for i in range(1, 11):
    info = list(cb(nums, i))
    for j in info:
        num = ''.join(list(map(str, reversed(j))))
        res.append(int(num))
res.sort()

if n >= len(res):
    print(-1)
else:
    print(res[n])

# 부품 찾기
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

s = 0
e = max(data)
res = 0

while s <= e:
    m = (s+e) // 2
    tot = 0

    for x in data:
        if x > m:
            tot += x - m

    if tot < m:
        e = m - 1
    else:
        s = m + 1
        res = tot
print(res)

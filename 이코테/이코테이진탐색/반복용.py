# 공유기 설치
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, c = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()
# 거리를 기준으로 이진 탐색하기
s = 1
e = data[-1] - data[0]
res = 0

while s <= e:
    m = (s+e) // 2
    val = data[0]
    cnt = 1

    for i in range(1, n):
        if data[i] >= m + val:
            val = data[i]
            cnt += 1

    if cnt >= c:
        s = m + 1
        res = m
    else:
        e = m - 1
print(res)

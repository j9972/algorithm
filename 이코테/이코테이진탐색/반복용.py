# 부품 찾기
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()


def count(a, find):
    return bisect_right(a, find) - bisect_left(a, find)


res = count(data, m)

if res != 0:
    print(res)
else:
    print(-1)

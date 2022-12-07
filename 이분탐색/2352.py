from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
res = []

# 교체를 하기 위한 함수


def binary(arr, target):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s+e) // 2
        if arr[m] <= target:
            s = m + 1
        else:
            e = m - 1
    return s


for d in data:
    if not res or res[-1] < d:
        res.append(d)
    else:
        res[binary(res, d)] = d
print(len(res))

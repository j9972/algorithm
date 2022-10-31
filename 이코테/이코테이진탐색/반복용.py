# 고정점 찾기
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))


def count_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx


def binary_search(a, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if a[mid] == mid:
        return mid
    elif a[mid] > mid:
        return binary_search(a, start, mid - 1)
    else:
        return binary_search(a, mid+1, end)


idx = binary_search(array, 0, n-1)

if idx == None:
    print(-1)
else:
    print(idx)

# 떡볶이 떡
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))


def count_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx


res = count_range(array, x, x)
if res != 0:
    print(res)
else:
    print(-1)


# def binary_search(a, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if a[mid] == target:
#         return mid
#     elif a[mid] > target:
#         return binary_search(a, target, start, mid - 1)
#     else:
#         return binary_search(a, target, mid+1, end)

    # while start <= end:
    #     mid = (start + end) // 2
    #     if a[mid] == target:
    #         return mid
    #     elif a[mid] > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    #     return None

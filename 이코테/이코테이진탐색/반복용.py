# 떡볶이 떡
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, target = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

res = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < target:
        end = mid - 1
    else:
        start = mid + 1
        res = mid
print(res)


def count_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx


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

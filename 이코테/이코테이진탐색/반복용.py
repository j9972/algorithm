# 고정점 찾기
from array import array
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()

start = 1
end = data[-1] - data[0]
res = 0


def count_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx


# def binary_search(a, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if a[mid] == mid:
#         return mid
#     elif a[mid] > mid:
#         return binary_search(a, start, mid - 1)
#     else:
#         return binary_search(a, mid+1, end)

while start <= end:
    count = 1
    val = data[0]
    mid = (start+end)//2

    for i in range(1, n):
        if data[i] >= val + mid:
            val = data[i]
            count += 1
    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)

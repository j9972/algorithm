# 부품 찾기
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort()

m = int(input())
x = list(map(int, input().split()))


def binary_search(a, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if a[mid] == target:
        return mid
    elif a[mid] > target:
        return binary_search(a, target, start, mid - 1)
    else:
        return binary_search(a, target, mid+1, end)

    # while start <= end:
    #     mid = (start + end) // 2
    #     if a[mid] == target:
    #         return mid
    #     elif a[mid] > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    #     return None


for i in x:
    res = binary_search(array, i, 0, n-1)
    if res != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

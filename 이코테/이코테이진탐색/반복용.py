from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort()


def binary_search(array, start, end):
    if start >= end:
        return None
    mid = (start+end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return binary_search(array, mid+1, end)
    else:
        return binary_search(array, start, mid-1)


idx = binary_search(array, 0, n-1)

if idx != None:
    print(idx)
else:
    print(-1)

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))

array.sort()


def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index


res = count_by_range(array, x, x)

if res:
    print(res)
else:
    print(-1)

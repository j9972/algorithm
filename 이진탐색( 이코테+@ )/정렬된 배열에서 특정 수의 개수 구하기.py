import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def count_range(a, find):
	return bisect_right(a, find) - bisect_left(a, find)

n, target = map(int,input().split())
data = list(map(int,input().split()))

if count_range(data,target) > 0:
    print(count_range(data,target))
else:
    print(-1)
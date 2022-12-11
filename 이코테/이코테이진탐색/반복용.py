# 부품 찾기
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
newData = list(map(int, input().split()))

data.sort()


def binary(arr, tar, s, e):
    while s <= e:
        m = (s+e) // 2
        if arr[m] == tar:
            return m
        elif arr[m] > tar:
            e = m - 1
        else:
            s = m + 1
    return None


for i in newData:
    res = binary(data, i, 0, n-1)
    if res != None:
        print('YES', end=' ')
    else:
        print('NO', end=' ')

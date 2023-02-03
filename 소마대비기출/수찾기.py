# 실버 4 - 1920
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

m = int(input())
test = list(map(int, input().split()))

data.sort()


def binary(arr, t, s, e):
    while s <= e:
        m = (s+e) // 2
        if arr[m] == t:
            return m
        elif arr[m] > t:
            e = m - 1
        elif arr[m] < t:
            s = m + 1
    return None


for i in test:
    res = binary(data, i, 0, n-1)
    if res != None:
        print(1)
    else:
        print(0)

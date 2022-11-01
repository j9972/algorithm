from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

res = []
res.append(data[0])


def binary(start, end, target):
    while start < end:
        mid = (start+end) // 2
        if res[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end


for i in range(1, n):
    if res[-1] < data[i]:
        res.append(data[i])
    else:
        # LIS
        lis = binary(0, len(res)-1, data[i])
        res[lis] = data[i]
print(n-len(res))

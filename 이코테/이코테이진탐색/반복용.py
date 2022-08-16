from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

# 최소 거리랑 최대 거리
start = 1
end = array[-1] - array[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1, n):
        if array[i] >= mid + value:
            value = array[i]
            count += 1
    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)

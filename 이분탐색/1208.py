from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


n, s = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

end = max(data)
start = data[0]
res = 0

while start < end:
    mid = (start + end) // 2
    sum = 0

    for n in data:
        if n > mid:
            sum += n - mid

    if sum == s:
        res += 1
        start = mid + 1
    else:
        end = mid - 1
print(res)

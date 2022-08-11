import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
res = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)

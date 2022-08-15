import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
res = 0

while start <= end:
    mid = (start + end) // 2
    total = 0  # 잘린 떡 조각 길이의 합

    for sliceArray in array:
        if sliceArray > mid:
            total += sliceArray - mid

    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)

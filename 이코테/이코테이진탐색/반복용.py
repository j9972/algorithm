import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = []

for i in range(n):
    array.append(int(input()))

array.sort()

# 최소 범위, 최대 범위
start = 1
end = array[-1] - array[0]

res = 0

while start <= end:
    mid = (start+end) // 2
    count = 1
    value = array[0]

    for i in range(1, n):
        if array[i] >= value + mid:
            count += 1
            value = array[i]

    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)

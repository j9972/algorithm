import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

start = 1
end = max(times) * n
res = 0

while start <= end:
    mid = (start+end) // 2
    total = 0

    for i in times:
        total += mid // i

    if total >= n:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)

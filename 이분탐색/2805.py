# 나무 자르기 - 떡볶이 떡 만들기랑 비슷
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
res = 0

while start <= end:
    mid = (start+end) // 2
    total = 0  # 잘린 나무들의 크기들의 합

    # 남아있는 나무의 크기를 생각하기
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)

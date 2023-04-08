import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def count_range(a, find):
	return bisect_right(a, find) - bisect_left(a, find)

n,c = map(int,input().split())

house = []
for i in range(n):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]
res=0

while start <= end:
    cnt = 1
    mid = (start + end) // 2
    val = house[0]

    for i in range(1,n):
        if house[i] >= val + mid:
            val = house[i]
            cnt += 1
    
    if cnt >= c:
        start = mid + 1
        res = mid  # 최적의 거리
    else:
        end = mid - 1
    
print(res)

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(map(int, input()))
array.sort()

# 최소 가능 거리, 최대 가능 거리
start = 1
end = array[-1] - array[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    count = 1c
    value = array[0]

    # 처음부터 하나하나 넣어본다 ( 현재 mid값을 통해 공유기 설치 )
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    # 거리를 늘릴수 있으면 늘리고, 없으면 줄인다
    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)

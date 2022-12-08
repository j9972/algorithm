import sys
input = sys.stdin.readline

n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()

s = 1
e = data[-1] - data[0]  # 최대 길이
res = 0

while s <= e:
    gap = (s+e) // 2
    cnt = 1  # 공유기 지금 설치한 개수
    val = data[0]  # 설치한 곳

    for i in range(1, n):
        # 가능 범위를 벗어난 경우 공유기 설치 ( 그 장소에 )
        if data[i] >= gap+val:
            val = data[i]
            cnt += 1

    if cnt >= c:
        s = gap + 1
        res = gap
    else:
        e = gap - 1
print(res)

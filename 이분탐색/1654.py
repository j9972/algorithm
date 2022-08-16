# 랜선 자르기 - 떡볶이 떡 자르기랑 비슷
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
array = []
for i in range(k):
    array.append(int(input()))


start = 1
end = max(array)

while start <= end:
    mid = (start+end) // 2
    total = 0

    for x in array:
        total += x // mid  # 전부 mid로 나눠서 나오는 갯수를 체크
    if total >= n:  # n은 나눠져야할 총 랜선의 개수
        start = mid + 1
    else:
        end = mid - 1

print(end)

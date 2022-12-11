# 카드 정렬
import heapq
import sys
input = sys.stdin.readline

data = []
n = int(input())
for i in range(n):
    data.append(int(input()))

heapq.heapify(data)
res = 0

while len(data) != 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)

    sumValue = one + two
    res += sumValue
    heapq.heappush(data, sumValue)
print(res)

# 카드 정렬하기
import sys
import heapq
input = sys.stdin.readline

n = int(input())
res = []

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sumValue = one + two
    res.append(sumValue)
    heapq.heappush(heap, sumValue)

print(sum(res))

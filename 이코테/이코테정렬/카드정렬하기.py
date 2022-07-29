import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

res = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sumValue = one + two
    res += sumValue
    heapq.heappush(heap, sumValue)
print(res)

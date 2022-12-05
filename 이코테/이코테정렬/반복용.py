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
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sumV = first + second
    res += sumV
    heapq.heappush(heap, sumV)
print(res)

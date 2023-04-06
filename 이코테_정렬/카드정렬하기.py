import sys
input = sys.stdin.readline
import heapq

heap = []
for i in range(int(input())):
    heap.append(int(input()))

heap.sort()
res = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)    
    heapq.heappush(heap,one+two)
    res += one + two
print(res)


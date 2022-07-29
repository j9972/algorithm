import sys
import heapq
input = sys.stdin.readline

n = int(input())

count = 0
heap = []
q = []

for _ in range(n):
    n, s, e = map(int, input().split())
    heapq.heappush(heap, [s, e, n])

s, e, n = heapq.heappop(heap)
heapq.heappush(q, e)

while heap:
    s, e, n = heapq.heappop(heap)
    if q[0] <= s:
        heapq.heappop(q)
    heapq.heappush(q, e)
print(len(q))

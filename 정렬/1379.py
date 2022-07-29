import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = sorted([list(map(int, input().split()))
             for _ in range(n)], key=lambda x: (x[1], x[2]))

lecture = [0 for _ in range(n+1)]
room = []

for i in range(1, n+1):
    heapq.heappush(room, i)

minHeap = []
# print(arr)
for num, start, end in arr:
    while minHeap and minHeap[0][0] <= start:
        e, r = heapq.heappop(minHeap)
        heapq.heappush(room, r)
    r = heapq.heappop(room)
    heapq.heappush(minHeap, [end, r])
    lecture[num] = r
print(max(lecture))
for x in lecture[1:]:
    print(x)

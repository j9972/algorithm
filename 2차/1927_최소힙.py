import sys
input = sys.stdin.readline

import heapq

q = []
for _ in range(int(input())):
    n = int(input())

    if n == 0:
        if len(q) == 0:
            print(0)
        else:
            val = heapq.heappop(q)
            print(val)
    else:
        heapq.heappush(q, n)
    
import sys
input = sys.stdin.readline

import heapq

n = int(input())
q = []

for _ in range(n):
    val = int(input())

    if val != 0:
        heapq.heappush(q, [abs(val), val])
    else:
        if len(q) == 0:
            print(0)
        else:
            abs_value, value_ = heapq.heappop(q)
            print(value_)

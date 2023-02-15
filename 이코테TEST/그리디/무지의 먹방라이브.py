import heapq
import sys
input = sys.stdin.readline


def sol(foods, k):
    length = len(foods)

    if sum(foods) <= k:
        return -1

    q = []
    for i in range(length):
        heapq.heappush(q, (foods[i], i+1))

    sumvalue = 0
    prev = 0

    while sumvalue + (q[0][0] - prev) * length < k:
        now = heapq.heappop(q)[0]
        sumvalue += (now - prev) * length
        prev = now
        length -= 1
    res = sorted(q, key=lambda x: x[1])

    return res[(k-sumvalue) % length][1]


print(sol([3, 1, 2], 5))

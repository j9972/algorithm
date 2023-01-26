from collections import deque
import heapq
import sys
input = sys.stdin.readline


def sol(food, k):
    length = len(food)

    if sum(food) <= k:
        return -1

    q = []
    res = []

    for i in range(length):
        heapq.heappush(q, (food[i], i+1))  # 음식번호, 음식 시간 순서

    previous = 0
    sum_value = 0

    while sum_value + ((q[0][0] - previous) * length) < k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        previous = now
        length -= 1

    res = sorted(q, key=lambda x: x[1])
    return res[(k-sum_value) % length][1]


print(sol([3, 1, 2], 5))

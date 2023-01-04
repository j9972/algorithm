import heapq
import sys
input = sys.stdin.readline


def solution(food_times, k):
    q = []
    length = len(food_times)

    if sum(food_times) <= k:
        return -1

    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))  # 시간, 노드번호+1 순서로 넣음

    totTime, prev = 0, 0

    while totTime + ((q[0][0] - prev)*length) < k:
        now = heapq.heappop(q)[0]
        totTime += (now - prev) * length
        prev = now
        length -= 1

    res = sorted(q, key=lambda x: x[1])

    print(res[(k-totTime) % length][1])


solution([3, 1, 2], 5)

import heapq
import sys
input = sys.stdin.readline


def sol(times, k):

    if sum(times) <= k:
        return -1

    length = len(times)

    q = []
    for i in range(length):
        heapq.heappush(q, (times[i], i+1))  # 시간이랑 번호

    sumValue = 0
    prev = 0

    while sumValue + ((q[0][0] - prev) * length) < k:
        now = heapq.heappop(q)[0]
        sumValue += (now - prev) * length
        prev = now
        length -= 1

    res = sorted(q, key=lambda x: x[1])

    print(res[(k-sumValue) % length][1])


sol([3, 1, 2], 5)

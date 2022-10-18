import heapq


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []

# 우선순위에 넣어짐을 제대로 알기 -> 8,6,4 라는 시간이 소요되는 음식들을 넣으면 4 -> 6 -> 8 순서로 우선순위에 맞춰서 들어간다
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))  # (음식시간, 음식번호)

    sumTime = 0
    prev = 0
    length = len(food_times)

    while sumTime + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        sumTime += (now - prev) * length
        length -= 1
        prev = now

    res = sorted(q, key=lambda x: x[1])

    return res[(k-sumTime) % length][1]

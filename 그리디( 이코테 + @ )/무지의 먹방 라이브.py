import heapq

def solution(food,k):
    if sum(food) <= k:
        return -1
    
    heap = []
    for i in range(len(food)):
        heapq.heappush(heap,(food[i], i+1))  # 음식 시간, idx 순서로 넣음
    
    tot = 0
    prev = 0
    length = len(food)

    while tot + (heap[0][0] - prev) * length <= k:
        now = heapq.heappop(heap)[0]
        tot += (now - prev) * length
        prev = now
        length -= 1
    
    res = sorted(heap, key=lambda x:x[1])

    return res[(k-tot)%length][1]

print(solution([3,1,2], 5))

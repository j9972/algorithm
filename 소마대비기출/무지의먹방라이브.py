import heapq

def sol(foods,k):
    q = []

    if sum(foods) <= k:
        return -1
    
    for i in range(len(foods)):
        heapq.heappush(q,(foods[i], i+1)) # 시간, 번호
    

    total = 0
    prev = 0
    length = len(foods)

    while total + (q[0][0] - prev) * length <= k:
        now = heapq.heappop(q)[0]
        total += (now-prev) * length
        prev = now
        length -= 1

    res = sorted(q, key=lambda x: x[1])

    return res[(k-total)%length][1]
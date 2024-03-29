# 무지의 먹방 라이브
import heapq
import sys
input = sys.stdin.readline

def solution(food_times, k):
    q = []
    length = len(food_times)
    
    if sum(food_times) <= k:
        return -1
    
    for i in range(length):
        heapq.heappush(q,(food_times[i], i+1))
    
    prev = 0
    st = 0
    
    while st + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        st += (now - prev) * length
        prev = now
        length -= 1
    
    res = sorted(q, key = lambda x : x[1])
    
    return res[(k-st) % length][1]
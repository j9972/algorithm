# 뉴스전하기
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []
for i in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))

bags = []
for i in range(k):
    bags.append(int(input()))
bags.sort()

res = 0
temp = []
for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewel)[1])
        if temp:
            res -= heapq.heappop(temp)
        elif not jewel:
            break
print(res)

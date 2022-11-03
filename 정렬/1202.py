import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

res = 0

jewel = []
for i in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))

bags = []
for i in range(k):
    bags.append(int(input()))
# heap을 쓰면 이렇게 안해도된다
# jewel = sorted(jewel, key=lambda x: (x[0], -x[1]))
bags.sort()

temp = []
for bag in bags:
    # jewel[0][0] => 첫번째 보석의 무게을 의미
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewel)[1])
    if temp:
        res -= heapq.heappop(temp)
    elif not jewel:
        break
print(res)

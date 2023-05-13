#1713 실버1
import sys
input = sys.stdin.readline
#from collections import deque
import heapq

n = int(input())
m = int(input())

candidate = {}
orders = list(map(int,input().split()))

for order in orders:
    if order not in candidate:
        if len(candidate) >= n:
            a = heapq.nsmallest(min(candidate), candidate, key=candidate.get)
            candidate.pop(a[0])
        candidate[order] = 1
    else:
        candidate[order] += 1

for ans in sorted(candidate.keys()):
    print(ans, end=' ')



# # [인덱스, 값]
# q = deque([])

# for order in orders:
#     if len(q) <= n:
#         time = len(q)
#         while True:
#             if time == 0:
#                 break
            
#             idx, value = q.popleft()
            
#             if idx == order:
#                 value += 1
            
#             q.append([idx,value])
#             time -= 1

#         q.append([order,1])
#         if len(q) > n:
#             cnt = m+1
#             check = 0
#             for _ in range(len(q)-1):
#                 idx, value = q.popleft()
                
#                 if value < cnt:
#                     cnt = value
#                     check = idx
                
#                 q.append([idx,value])
            
#             if cnt >= 2:
#                 q.popleft()
#             # else:
#             #     for i in range(len(q)-1):
#             #         if check == q[i][0]:
#             #             q.pop(i)
# print(q)
                

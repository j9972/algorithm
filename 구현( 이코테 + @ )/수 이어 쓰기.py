# 1748 실버 4
import sys
input = sys.stdin.readline
from collections import deque
import heapq

n = int(input())

# try 1,2,3 -> 모두 시간 초과
# n = int(input())
# #num = ''
# #cnt = 0

# for i in range(1,n+1):
#     cnt += len(str(i))
#     #num += str(i)
# print(cnt)
# #print(len(num))

# heap = []

# for i in range(1,n+1):
#     for j in str(i):
#         heapq.heappush(heap,j)

# print(len(heap))

# heap = [str(i) for i in range(1,n+1) if len(str) >= 2 else str(i).split()]
# print(heap)

# try 4 는 메모리 초과
# q = deque()
# for i in range(1,n+1):
#     q.append(str(i))
# cnt = 0
# while q:
#     data = q.popleft()
#     cnt += len(data)
# print(cnt)

length = len(str(n))
ans = 0

for i in range(length - 1):
    ans += 9 * (10 ** i) * (i+1)
#print(ans)
print(ans + (n-(10**(length-1)) + 1) * length)
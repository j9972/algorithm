#골드2 - 2812
import sys
input = sys.stdin.readline
#from itertools import combinations as cb

n, K =map(int,input().split())
data = list(input())
stack = []
k = K

for i in range(n):
    while k > 0 and stack and stack[-1] < data[i]:
        stack.pop()
        k -= 1
    stack.append(data[i])
print(''.join(stack[:n-K]))

# 메모리 초과
# value = list(cb(data,n-k))
# mv = 0
# for i in value:
#     ans = int(''.join(i))
#     if mv < ans:
#         mv = ans
# print(mv)
# 1722 - 골5
import sys
input = sys.stdin.readline
from itertools import permutations as pm

n = int(input())
data = list(map(int,input().split()))

def fact(n):
    if n == 1 or n == 2:
        return n
    else: 
        return n * fact(n-1)

def find(n):
    k = data[1]
    a = ''
    for i in range(1,n+1):
        if k <= fact(n) // n * i:
            a += str(i)
        else:
            continue
    return a

if data[0] == 1:
    k = data[1]
    a = 0
    for i in range(1,n+1):
        if k < fact(n) // n * i:
            a = i
            break
    if k == fact(n) // n:
else:


    

# value = [i for i in range(1,n+1)]
# res = list(pm(value,n))

# # def permutations(elements):
# #     if len(elements) == 1:
# #         return [elements]
# #     result = []
# #     for i in range(len(elements)):
# #         remaining_elements = elements[:i] + elements[i+1:]
# #         for p in permutations(remaining_elements):
# #             result.append([elements[i]] + p)
# #     return result

# # res = permutations(value)

# if data[0] == 1:
#     for i in res[data[1]-1]:
#         print(i, end=' ')  
# elif data[0] == 2:
#     cnt = 0
#     ans = ''
#     for i in data[1:]:
#         ans += str(i)
#     for i in res:
#         cnt += 1
#         tmp = ''
#         for j in i:
#             tmp += str(j)
#         if tmp == ans:
#             print(cnt)
#             break



import sys
from itertools import combinations as cb

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# print("arr: {}".format(arr))
# print("*arr: {} , zip(*arr) : {}".format(*arr, zip(*arr)))

mem = [sum(i) + sum(j) for i,j in zip(arr, zip(*arr))]

# for i,j in zip(arr, zip(*arr)):
#     print(i,j)
#     print(sum(i) , sum(j))

#print(mem)

tot = sum(mem) // 2

res = sys.maxsize

for i in cb(mem, n//2):
    res = min(res, abs(tot - sum(i)))
print(res)
import sys
input = sys.stdin.readline
from itertools import combinations as cb

length = int(input())
s = list(map(int,input().split()))
n = int(input())
res = []

s.sort()

if n in s:
    print(0)
else:

    start = 0
    end = 0
    for i in s:
        if i < n:
            start = i + 1
        elif i > n:
            end = i
            break
    
    for i in range(start,end):
        if i > 0:
            res.append(i)
    
    tot = len(list(cb(res,2)))

    for data in list(cb(res,2)):
        if data[0] > n or data[1] < n:
            tot -= 1
    print(tot)
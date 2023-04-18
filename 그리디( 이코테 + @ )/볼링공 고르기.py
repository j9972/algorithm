from itertools import combinations as cb

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

cnt = 0
for i in list(cb(data,2)):
    if i[0] != i[1]:
        cnt += 1
print(cnt)
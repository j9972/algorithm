import sys

t,a,b = map(int,input().split())

arr = [
    list(input().split())
    for _ in range(t)
]

visited = ['.' for _ in range(1001)]

for alpha, idx in arr:
    visited[int(idx)] = alpha

cnt = 0

for i in range(a,b+1):
    min_dist_s, min_dist_n = sys.maxsize, sys.maxsize

    for j in range(1001):
        
        if visited[j] == 'S':
            min_dist_s = min(min_dist_s, abs(i-j)+1)
            
        if visited[j] == 'N':
            min_dist_n = min(min_dist_n, abs(i-j)+1)
        
    
    if min_dist_s <= min_dist_n:
        cnt += 1
print(cnt)

import sys

t,a,b = map(int,input().split())

arr = [
    list(input().split())
    for _ in range(t)
]

cnt = 0

for i in range(a,b+1):
    min_dist_n, min_dist_s = sys.maxsize, sys.maxsize

    for alpha, idx in arr:
        idx = int(idx)

        if alpha == 'S':
            min_dist_s = min(min_dist_s, abs(idx - i))
        if alpha == 'N':
            min_dist_n = min(min_dist_n, abs(idx - i))

    if min_dist_s <= min_dist_n:
        cnt += 1
print(cnt)
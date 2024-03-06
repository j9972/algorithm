from itertools import combinations as cb
import sys

n = int(input())
min_val = sys.maxsize

num = [i for i in range(n)]

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

half = list(cb(num, n//2))

other_half = []
for i in half:
    tmp = []
    for j in range(n):
        if j not in i:
            tmp.append(j)
    other_half.append(tmp)

for i in range(len(half)):
    inner_half = list(cb(half[i], 2))
    inner_other_half = list(cb(other_half[i], 2))

    cnt1,cnt2 = 0,0

    for j in inner_half:
        x,y = j
        cnt1 += arr[x][y]
        cnt1 += arr[y][x]

    for j in inner_other_half:
        x,y = j
        cnt2 += arr[x][y]
        cnt2 += arr[y][x]
        
    min_val = min(min_val, abs(cnt2 - cnt1))
print(min_val)




import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_h = max(map(max, arr))
min_h = min(map(min, arr))

dic = {}
for i in range(n):
    for j in range(m):
        if arr[i][j] in dic:
            dic[arr[i][j]] += 1
        else:
            dic[arr[i][j]] = 1

min_time = 10**9
ans = 0

for h in range(min_h, max_h+1):
    plus, minus = 0,0

    for height, cnt in dic.items():
        if height < h:
            plus += cnt * abs(height - h)
        elif height > h:
            minus += cnt * abs(height - h)
    
    if minus + b >= plus:
        if min_time >= plus + minus  * 2:
            min_time = plus + minus * 2
            ans = h

print(min_time, ans)

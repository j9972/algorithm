import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))

start, ans, end = 0,0,max(tree)

while start <= end:
    mid = (start + end) // 2
    tot = 0

    for i in tree:
        if i > mid:
            tot += i - mid
    
    if tot < m:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)
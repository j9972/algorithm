import sys
input = sys.stdin.readline

n, target = map(int,input().split())
riceCake = list(map(int,input().split()))

start = 0
end = max(riceCake)

res = 0
while start <= end:
    tot = 0
    mid = (start+end) // 2

    for dd in riceCake:
        if dd > mid:
            tot += dd - mid
    
    if tot < target:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
        

print(res)

        
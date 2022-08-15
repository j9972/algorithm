import sys
input = sys.stdin.readline

N, T = map(int, input().split())
res = []
for _ in range(N):
    time, gap, n = map(int, input().split())
    li = [time+gap*i for i in range(n)]
    if li[-1] < T:
        continue
    start, end = 0, n-1
    a = 0
    while start <= end:
        mid = (start+end)//2
        if li[mid] >= T:
            a = mid
            end = mid-1
        else:
            start = mid+1
    res.append(li[a]-T)
print(min(res) if res else -1)

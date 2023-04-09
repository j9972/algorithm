import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

#data.sort() -> 강의 순서 유지 ## 

start = max(data)# 최소 길이 후보
end = sum(data)# 최대 길이 후보
res = 0

while start <= end:
    mid = (start+end) // 2
    tot = 0
    cnt = 1
    
    for d in data:
        if tot + d <= mid:
            tot += d
        else:
            tot = d
            cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = mid
        

print(res)
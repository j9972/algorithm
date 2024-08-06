import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

min_val = sys.maxsize

ans = []

def getDist():
    max_dist = 0
    length = len(ans)

    for i in range(length):
        for j in range(i+1,length):
            x1,y1 = ans[i]
            x2,y2 = ans[j]

            max_dist = max(max_dist, (x2-x1)**2 + (y2-y1)**2)
    return max_dist

def choose(idx, cnt):
    global min_val

    if idx == n:
        if cnt == m:
            min_val = min(min_val, getDist())
        return
    
    ans.append(arr[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)

choose(0,0)
print(min_val)
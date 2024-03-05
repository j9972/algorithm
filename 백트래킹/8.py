n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

ans = [1] * k # 움직이는 윷들

max_val = 0

def Print():
    global max_val
    cnt = 0
    for i in ans:
        if i >= m:
            cnt += 1
    max_val = max(max_val, cnt)

def choose(cnt):
    if cnt == n:
        Print()
        return
    
    for i in range(k):
        if ans[i] >= m:
            continue
        
        ans[i] += arr[cnt]
        choose(cnt + 1)
        ans[i] -= arr[cnt]
    
    Print()
    return

choose(0)
print(max_val)
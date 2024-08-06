n,m = map(int,input().split())
arr = list(map(int,input().split()))

ans = []
max_val = 0

def Print():
    data = 0
    for e in ans:
        data ^= e
    
    return data


def choose(idx, cnt):
    global max_val
    
    if idx == n:
        if cnt == m:
            max_val = max(max_val, Print())
        return
    
    ans.append(arr[idx])
    choose(idx+1,  cnt + 1)
    ans.pop()
    choose(idx+1, cnt)

choose(0,0)
print(max_val)


import sys

n,m = map(int,input().split())
arr = list(map(int,input().split()))

max_val = -sys.maxsize
ans = list()

def calc():
    val = 0
    for i in ans:
        val ^= i
    return val

def choose(idx, cnt):
    global max_val

    if cnt == m:
        max_val = max(max_val, calc())
        return

    if idx == n:
        return
    
    ans.append(arr[idx])
    choose(idx + 1, cnt + 1)
    ans.pop()
    choose(idx + 1, cnt)

choose(0,0)
print(max_val)
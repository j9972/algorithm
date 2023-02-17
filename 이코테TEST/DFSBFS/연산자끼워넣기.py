import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

add,minus,multi,div = map(int,input().split())
mxv = int(-1e9)
miv = int(1e9)

def dfs(i,now):
    global add,minus,multi,div,mxv,miv
    if i == n:
        mxv = max(mxv, now)
        miv = min(miv, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now - data[i])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(i+1, now * data[i])
            multi += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1
dfs(1,data[0])
print(mxv)
print(miv)
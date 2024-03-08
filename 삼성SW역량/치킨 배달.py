import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans, home, chicken = list(), list(), list()
min_dist = sys.maxsize

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))

def calc():
    dist = 0
    for x,y in home:
        tmp = sys.maxsize
        for idx in ans:
            i,j = chicken[idx]
            tmp = min(tmp, abs(x-i) + abs(y-j))
        dist += tmp
    return dist

def choose(idx, cnt):
    global min_dist

    if idx > len(chicken):
        return
    
    if cnt == m:
        min_dist = min(min_dist, calc())
        return
    
    ans.append(idx)
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)

choose(0,0)
print(min_dist)
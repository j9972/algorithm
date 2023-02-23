#실버 3 - 15651
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
res= []

def dfs():
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    else:
        for i in range(1,n+1):
            res.append(i)
            dfs()
            res.pop()
dfs()
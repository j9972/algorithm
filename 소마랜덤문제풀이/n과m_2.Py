# 실버3 - 15650
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
res = []

def dfs(start):
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    else:
        for i in range(start,n+1):
            if i not in res:
                res.append(i)
                dfs(i+1)
                res.pop()
dfs(1)
#실버 3 - 15654
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
data = list(map(int,input().split()))
data.sort()

res = []

def dfs():
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    else:
        for i in range(n):
            if i not in res:
                res.append(data[i])
                dfs()
                res.pop()
dfs()

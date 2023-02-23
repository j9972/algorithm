#실버 3 - 15654
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
data = list(map(int,input().split()))
data.sort()

res = []
visit = [False] * n

def dfs():
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    else:
        for i in range(n):
            if not visit[i]:
                res.append(data[i])
                visit[i] = True
                dfs()
                visit[i] = False
                res.pop()
dfs()

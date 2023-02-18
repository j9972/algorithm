# 실버3 - 15649
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

data = []

def dfs():
    if len(data) == m:
        print(' '.join(map(str, data)))
        return
    for i in range(1,n+1):  
        if i not in data:
            data.append(i)
            dfs()
            data.pop()
dfs()


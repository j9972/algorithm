# 실버3 - 15652 - 다시
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = []


def dfs(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    for i in range(start, n+1):
        res.append(i)
        dfs(i)
        res.pop()


dfs(1)

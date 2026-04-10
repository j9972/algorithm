import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

n,k = map(int,input().split())

dp = [0] * 100001

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()

        if cur == k:
            return dp[k]

        for i in (cur+1, cur-1, cur*2):
            if 0<=i<=100000 and dp[i] == 0:
                dp[i] = dp[cur] + 1
                q.append(i)
print(bfs(n))


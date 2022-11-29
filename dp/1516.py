import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
cost = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    tmp = list(map(int, input().split()))[:-1]
    cost[i] = tmp[0]
    for j in tmp[1:]:
        graph[j].append(i)
        inDegree[i] += 1

q = deque()

for i in range(1, n+1):
    if not inDegree[i]:
        q.append(i)
        dp[i] = cost[i]

while q:
    n = q.popleft()

    for i in graph[n]:
        inDegree[i] -= 1
        dp[i] = max(dp[i], dp[n] + cost[i])

        if not inDegree[i]:
            q.append(i)

for i in range(1, n+1):
    print(dp[i], end='\n')

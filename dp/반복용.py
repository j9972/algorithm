# 1005
from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))

    k_way = [[] for _ in range(n+1)]

    inDegree = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]

    queue = deque()

    for i in range(k):
        a, b = map(int, input().split())
        k_way[a].append(b)
        inDegree[b] += 1

    target = int(input())

    for i in range(1, n+1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = time[i-1]

    while queue:
        tmp = queue.popleft()

        for i in k_way[tmp]:
            inDegree[i] -= 1
            dp[i] = max(dp[i], time[i-1] + dp[tmp])
            if inDegree[i] == 0:
                queue.append(i)

    print(dp[target])

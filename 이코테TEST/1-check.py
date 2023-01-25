import copy
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
inDegree = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 도착 위치를 알려줌
    for j in data[1:-1]:  # 출발 위치임
        graph[j].append(i)
        inDegree[i] += 1


q = deque()
res = copy.deepcopy(time)

for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        res[i] = max(res[i], res[now] + time[i])
        inDegree[i] -= 1

        if inDegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(res[i])

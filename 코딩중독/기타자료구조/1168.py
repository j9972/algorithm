import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N+1)])
res = []
while dq:
    dq.rotate(-K+1)
    res.append(str(dq.popleft()))
sys.stdout.write("<"+", ".join(res)+">")

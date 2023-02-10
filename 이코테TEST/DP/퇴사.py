import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
t = []
p = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

d = [0] * (n+1)

mv = 0

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        d[i] = max(p[i] + d[time], mv)
    else:
        mv = d[i]
print(max(d))

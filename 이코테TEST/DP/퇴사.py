import sys
input = sys.stdin.readline

t = []
p = []
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

d = [0] * (n+1)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        d[i] = max(d[i], p[i] + d[time])
        
print(d[n])

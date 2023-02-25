import sys
input = sys.stdin.readline

n = int(input())

t = []
p = []

d = [0] * (n+1)

for i in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

mv = 0
for i in range(n-1,-1,-1):
    time = t[i] + i
    if time <= n:
        d[i] = max(mv, d[time]+ p[i])
        mv = d[i]
    else:
        d[i] = mv
print(mv)
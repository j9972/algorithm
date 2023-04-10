import sys
input = sys.stdin.readline

t = []
p = []

n = int(input())

for i in range(n):
    time, price = map(int,input().split())
    t.append(time)
    p.append(price)

d = [0] * (n+1)

mv = 0
for i in range(n-1,-1,-1):
    time = t[i] + i # 1일 + t[i] ( t[i] = 3) -> 1일차에 진행하는 일이 3일짜리면 4일차부터 할수있응꼐 이래됨
    if time <= n:
        d[i] = max(d[time] + p[i], d[i])
        mv = d[i]
    else:
        d[i] = mv

print(mv)

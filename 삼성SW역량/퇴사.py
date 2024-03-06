import sys

n = int(input())
time, price = list(), list()

for i in range(n):
    a,b = map(int,input().split())
    time.append(a)
    price.append(b)

d = [0] * (n+1)

val = 0
for i in range(n-1,-1,-1):
    if time[i] + i > n:
        d[i] = val
    else:
        d[i] = max(d[time[i] + i] + price[i], val)
        val = d[i]
print(val)
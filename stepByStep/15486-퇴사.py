n = int(input())

time = [0 for _ in range(n+1)]
price = [0 for _ in range(n+1)]
d = [0 for _ in range(n+1)]

for i in range(1,n+1):
    time[i], price[i] = map(int,input().split())

for i in range(1,n+1):
    d[i] = max(d[i], d[i-1])

    date = time[i] + i - 1

    if date <= n:
        d[date] = max(d[date], d[i-1] + price[i])
print(max(d))
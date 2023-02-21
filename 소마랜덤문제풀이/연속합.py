# 실버2 - 1912

n = int(input())
data = list(map(int,input().split()))
INF = int(-1e9)
d = [INF] * (n+1)

d[0] = data[0]
for i in range(1,n):
    d[i] = max(data[i], d[i-1]+data[i])
print(max(d))
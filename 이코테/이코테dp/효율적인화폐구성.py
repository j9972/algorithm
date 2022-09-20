n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

d = [0] * 1001

for i in range(n):
    for j in range(data[i], m+1):
        if d[j-data[i]] != 1001:
            d[i] = min(d[j], d[j-data[i]]+1)

if d[m] == 1001:
    print(-1)
else:
    print(d[m])

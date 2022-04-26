n = int(input())
d = [[0] * 10 for _ in range(1001)]

for i in range(10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j] + d[i][j-1]

print(sum(d[n]) % 10007)

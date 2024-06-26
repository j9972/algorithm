n = int(input())
arr = list(map(int,input().split()))

d = [
    [0] * 21
    for _ in range(n-1)
]

d[0][arr[0]] = 1

for i in range(1,n-1):
    for j in range(21):
        if j - arr[i] >= 0:
            d[i][j-arr[i]] += d[i-1][j]
        if j + arr[i] <= 20:
            d[i][j+arr[i]] += d[i-1][j]
print(d[-1][arr[-1]])
n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

d[0][0] = 1

for i in range(n):
    for j in range(n):
        dist = arr[i][j]

        if i == j == n-1:
            print(d[i][j])
            break

        if i + dist < n:
            d[i+dist][j] += d[i][j]
        if j + dist < n:
            d[i][j+dist] += d[i][j]
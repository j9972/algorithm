n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

d = [
    [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for _ in range(3)
]

# 0가로, 1세로, 2대각
d[0][0][1] = 1
for i in range(2,n):
    if arr[0][i] == 0:
        d[0][0][i] = d[0][0][i-1]

for i in range(1,n):
    for j in range(1,n):

        # 대각
        if arr[i][j] == 0 and arr[i][j-1] == 0 and arr[i-1][j] == 0:
            d[2][i][j] = d[0][i-1][j-1] + d[1][i-1][j-1] + d[2][i-1][j-1]

        # 세로, 가로
        if arr[i][j] == 0:
            d[0][i][j] = d[0][i][j-1] + d[2][i][j-1]
            d[1][i][j] = d[1][i-1][j] + d[2][i-1][j]

print(d[0][n-1][n-1] + d[1][n-1][n-1] + d[2][n-1][n-1])
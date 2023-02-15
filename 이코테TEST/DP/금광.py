import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    idx = 0

    d = []
    info = list(map(int, input().split()))
    for i in range(n):
        d.append(info[idx:idx+m])
        idx += m

    for j in range(1, m):
        for i in range(1, n):
            if i == 0:
                left_up = 0
            else:
                left_up = d[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = d[i+1][j-1]
            left = d[i][j-1]

            d[i][j] += max(left, left_down, left_up)
    res = 0
    for i in range(n):
        res = max(res, d[i][m-1])
    print(res)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

for tc in range(int(input())):
    n, m = map(int, input().split())

    data = list(map(int, input().split()))
    idx = 0

    d = []
    for i in range(m):
        d.append(data[idx:idx+m])
        idx += m

    for j in range(1, m):
        for i in range(n):
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
        res = max(res, d[i][m-1])  # 맨 마지막줄에서 맨 위부터 맨 아래 까지 체크

    print(res)

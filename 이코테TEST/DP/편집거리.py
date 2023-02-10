import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def sol(str1, str2):
    n = len(str1)
    m = len(str2)

    d = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        d[i][0] = i
    for i in range(1, n+1):
        d[0][i] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i-1][j-1], d[i-1][j], d[i][j-1])

    return d[n][m]


print(sol('cat', 'cut'))

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
p, m, mu, d = map(int, input().split())

maxv = int(-1e9)
minv = int(1e9)


def dfs(i, now):
    global maxv, minv, p, m, mu, d
    if i == n:
        maxv = max(maxv, now)
        minv = min(minv, now)
    else:
        if p > 0:
            p -= 1
            dfs(i+1, now + data[i])
            p += 1
        elif m > 0:
            m -= 1
            dfs(i+1, now - data[i])
            m += 1
        elif mu > 0:
            mu -= 1
            dfs(i+1, now * data[i])
            mu += 1
        elif d > 0:
            d -= 1
            dfs(i+1, int(now / data[i]))
            d += 1


dfs(1, data[0])
print(maxv)
print(minv)

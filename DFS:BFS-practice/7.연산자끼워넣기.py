n = int(input())

data = list(map(int, input().split()))

ad, mi, mu, di = map(int, input().split())

maxNum = -1e9
minNum = 1e9


def dfs(i, now):
    global maxNum, minNum, ad, mi, mu, di

    if i == n:
        maxNum = max(maxNum, now)
        minNum = min(minNum, now)
        return
    if ad > 0:
        ad -= 1
        dfs(i+1, now + data[i])

    if mi > 0:
        mi -= 1
        dfs(i+1, now - data[i])

    if mu > 0:
        mu -= 1
        dfs(i+1, now * data[i])

    if di > 0:
        di -= 1
        dfs(i+1, int(now / data[i]))


dfs(1, data[0])
print(maxNum)
print(minNum)

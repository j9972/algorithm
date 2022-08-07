n = int(input())

data = list(map(int, input().split()))

add, minus, multi, div = map(int, input().split())

maxValue = -10e9
minValue = 10e9


def dfs(i, now):
    global maxValue, minValue, minus, add, multi, div
    if i == n:
        minValue = min(minValue, now)
        maxValue = max(maxValue, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now - data[i])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(i+1, now * data[i])
            multi += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1


dfs(1, data[0])

print(maxValue)
print(minValue)

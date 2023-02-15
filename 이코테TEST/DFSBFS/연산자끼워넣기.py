import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

maxValue = int(-1e9)
minValue = int(1e9)


def dfs(i, now):
    global maxValue, minValue, plus, minus, multi, div
    if i == n:
        maxValue = max(maxValue, now)
        minValue = min(minValue, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now + data[i])
            plus += 1
        elif minus > 0:
            minus -= 1
            dfs(i+1, now - data[i])
            minus += 1
        elif multi > 0:
            multi -= 1
            dfs(i+1, now * data[i])
            multi += 1
        elif div > 0:
            div -= 1
            dfs(i+1,  int(now / data[i]))
            div += 1


dfs(1, data[0])
print(maxValue)
print(minValue)

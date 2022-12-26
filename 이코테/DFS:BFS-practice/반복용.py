from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

maxValue = -10e9
minValue = 10e9

data = list(map(int, input().split()))

add, minus, multi, div = map(int, input().split())


def dfs(i, now):
    global maxValue, minValue, add, minus, multi, div
    if i == n:
        maxValue = max(maxValue, now)
        minValue = min(minValue, now)
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

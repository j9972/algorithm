from collections import deque
import sys
sys.setrecursionlimit(10**9)

n = int(input())

data = list(map(int, input().split()))

plus, minus, multi, div = map(int, input().split())

minvalue = 10e9
maxValue = -10e9


def dfs(i, now):
    global plus, minus, multi, div, maxValue, minvalue

    if i == n:
        minvalue = min(minvalue, now)
        maxValue = max(maxValue, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now + data[i])
            plus += 1
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
            dfs(i+1, now / int(data[i]))
            div += 1


dfs(1, data[0])

print(maxValue)
print(minvalue)

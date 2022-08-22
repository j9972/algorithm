import sys


import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

house = []
chicken = []

# check
for r in range(n):
    board = list(map(int, input().split()))
    for c in range(n):
        if board[c] == 1:
            house.append((r, c))
        elif board[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))


def getSum(candidate):
    res = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in chicken:
            temp = min(temp, abs(hx, cx)+abs(hy-cy))
        res += temp
    return res


res = 1e9
for c in candidates:
    res = min(res, getSum(c))
print(res)

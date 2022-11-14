# 만들 수 없는 금액
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

res = list(combinations(data, 2))

count = 0
for i in res:
    if i[0] == i[1]:
        count += 1

print(len(res) - count)

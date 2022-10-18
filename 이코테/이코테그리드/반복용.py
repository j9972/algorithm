# 만들 수 없는 금액
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

choosing = list(combinations(data, 2))  # 2개 뽑는 모든 조합

count = len(choosing)
for i in range(len(choosing)):
    if choosing[i][0] == choosing[i][1]:
        count -= 1

print(count)

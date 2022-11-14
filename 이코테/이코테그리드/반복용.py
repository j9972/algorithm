# 만들 수 없는 금액
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))

coin.sort()

t = 1
for i in coin:
    if t < i:
        break
    t += i
print(t)

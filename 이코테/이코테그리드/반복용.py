# 모험가 길드
import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

g = 0
c = 0
for i in data:
    c += 1
    if c >= i:
        g += 1
        c = 0

print(g)

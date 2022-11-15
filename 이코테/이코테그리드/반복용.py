# 무지의 먹방 라이브
import heapq
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

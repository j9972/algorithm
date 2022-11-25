# 숫자 카드 게임
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

d = []
for i in range(n):
    d.append(min(data[i]))

print(max(d))

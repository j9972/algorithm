import sys
from tokenize import group
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt, group = 0, 0
for i in data:
    cnt += 1
    if cnt >= i:
        group += 1
        cnt = 0
print(group)

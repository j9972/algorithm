import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
cnt = 0
for i in data:
    cnt += 1
    if cnt >= i:
        group += 1
        cnt = 0
print(group)

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

data.sort()

group = 0
cnt = 0
x = 1
for i in range(n):
    cnt += 1
    if cnt >= x:
        group += 1
        x += 1
        cnt = 0
print(group)
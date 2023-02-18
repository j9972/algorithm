import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

data.sort()

cnt = 1
for i in data:
    if cnt < i:
        break
    cnt += i
print(cnt)

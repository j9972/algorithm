import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

data.sort()

cnt =0
group = 0
for i in range(len(data)):
    cnt += 1
    if cnt >= i:
        group += 1
        cnt = 0
print(group)
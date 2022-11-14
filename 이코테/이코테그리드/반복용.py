# 모험가 길드
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()
res = []
totalCount = 0

for i in data:
    res.append(i)
    if i == res.count(i):
        totalCount += 1


print(totalCount)

# for i in data:
#     count += 1
#     if count >= i:
#         res += 1
#         count = 0

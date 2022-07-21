import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# 공포도를 오름차순으로 나누기
data.sort()

# 그룹수
groupCount = 0
# 인원
count = 0

for i in data:
    count += 1
    if count >= i:
        groupCount += 1
        count = 0
print(groupCount)

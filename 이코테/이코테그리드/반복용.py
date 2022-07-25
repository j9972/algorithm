n = int(input())
data = list(map(int, input().split()))

count = 0
teamCount = 0

data.sort()

for i in data:
    count += 1
    if count == i:
        teamCount += 1
        count = 0
print(teamCount)

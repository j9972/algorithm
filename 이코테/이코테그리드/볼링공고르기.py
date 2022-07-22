from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

res = list(combinations(data, 2))

count = 0
for i in range(len(res)):
    if res[i][0] == res[i][1]:
        count += 1

print(len(res)-count)

from itertools import combinations
number = '1924'
k = 2
num = len(number) - k
res = list(combinations(number, num))
ans = list(res)
data = []
for i in range(len(ans)):
    data.append(''.join(ans))

print(data)

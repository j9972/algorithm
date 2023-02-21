# 실버2 - 1541
import sys
input = sys.stdin.readline

a = input().split('-')
res = []

for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    res.append(cnt)

f = res[0]
for i in range(1,len(res)):
    f -= res[i]
print(f)
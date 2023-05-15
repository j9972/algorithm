# 2331 실버4
import sys
input = sys.stdin.readline

a, p = map(str,input().rstrip().split())

d = [a]

while True:
    cnt = 0
    for i in d[-1]:
        cnt += int(i) ** int(p)

    if str(cnt) not in d:
        d.append(str(cnt))
    else:
        d.append(str(cnt))
        break

cnt = 0
for i in d:
    if i != d[-1]:
        cnt += 1
    else:
        break

print(cnt)
    
# 실버4 - 2870
import sys
input = sys.stdin.readline

n = int(input())
res = []

for i in range(n):
    s = input().rstrip()
    ans = ""

    for i in s:
        if ord(i) < 97:
            ans += i
        else:
            if ans:
                res.append(int(ans))
                ans = ''
    if ans:
        res.append(int(ans))

res.sort()
for i in res:
    print(i)
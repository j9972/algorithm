# 곱하기 혹은 더하기
import sys
input = sys.stdin.readline

n = input()
s = list(n)
print(s)
res = 0

for i in range(len(s)-1):
    if int(s[i]) == 0 or int(s[i]) == 1 or res == 0 or res == 1:
        res += int(s[i])
    else:
        res *= int(s[i])

print(res)

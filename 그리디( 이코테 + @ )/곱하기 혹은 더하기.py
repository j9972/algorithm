import sys
input = sys.stdin.readline

n = input().rstrip()
res = 0
for i in n:
    if int(i) == 0 or int(i) == 1 or res == 0 or res == 1:
        res += int(i)
    else:
        res *= int(i)
print(res)
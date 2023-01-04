import sys
input = sys.stdin.readline

s = input().rstrip()
ans = 0

for i in s:
    if i == '0' or i == '1' or ans == 0:
        ans += int(i)
    else:
        ans *= int(i)
print(ans)

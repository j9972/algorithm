import sys
input = sys.stdin.readline

s = input().rstrip()
zero = 0
one = 0

if s[0] == '0':
    one += 1
else:
    zero += 1

for i in range(1, len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            one += 1
        else:
            zero += 1
print(min(one, zero))

# 곱하기 혹은 더하기
import sys
input = sys.stdin.readline

n = input()
s = list(n)

zero = 0
one = 0

if s[0] == '0':
    one = 1
elif s[0] == '1':
    zero = 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            zero += 1
        else:
            one += 1
print(min(zero, one))

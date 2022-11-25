# 문자열 뒤집기
import heapq
import sys
input = sys.stdin.readline

s = input()

zero = one = 0

if s[0] == '0':
    one += 1
else:
    zero += 1

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        if s[i] == '0':
            one += 1
        else:
            zero += 1

print(min(one, zero))

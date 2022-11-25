# 곱하기 혹은 더하기
import heapq
import sys
input = sys.stdin.readline

s = input()

count = 0
for i in range(len(s)-1):
    if s[i] == '0' or count == 0 or s[i] == '1':
        count += int(s[i])
    else:
        count *= int(s[i])

print(count)

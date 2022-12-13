# 왕실의 나이트
import sys
input = sys.stdin.readline

data = input()
col = int(ord(data[0])) - int(ord('a')) + 1
row = int(data[1])

step = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

res = 0

for s in step:
    next_row = row + s[1]
    next_col = col + s[0]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        res += 1
print(res)

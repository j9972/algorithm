# 왕실의 나이트
import sys
input = sys.stdin.readline

data = input()
# a3, a는 열(col), 3은 행(row)
col = int(data[1])
row = int(ord(data[0])) - int(ord('a')) + 1

step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
count = 0

for i in step:
    next_col = col + i[1]
    next_row = row + i[0]
    if 1 <= next_col <= 8 and 1 <= next_row <= 8:
        count += 1
print(count)

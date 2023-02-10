import sys
input = sys.stdin.readline

s = input()
row = int(s[1])
col = int(ord(s[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]
res = 0
for step in steps:
    next_col = col + step[1]
    next_row = row + step[0]

    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        res += 1
print(res)

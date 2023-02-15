import sys
input = sys.stdin.readline

s = input()

row = int(s[1])
col = int(ord(s[0])) - int(ord('a')) + 1

step = [(-1, -2), (1, -2), (-1, 2), (1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
cmt = 0
for s in step:
    next_col = col + s[1]
    next_row = row + s[0]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        cmt += 1
print(cmt)

import sys
input = sys.stdin.readline

direction = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (-2, 1), (2, 1), (-1, 2), (1, 2)]

s = input()
col = int(ord(s[0])) - int(ord('a')) + 1
row = int(s[1])

res = 0
for i in direction:
    next_row = i[0] + row
    next_col = i[1] + col

    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        res += 1
print(res)

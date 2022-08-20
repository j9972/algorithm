input_data = input()

# 열 행 순서

# 행
row = int(input_data[1])
# 열
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (1, -2), (-1, 2), (1, 2)]


res = 0
for s in steps:
    next_row = row + s[1]
    next_column = column + s[0]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        res += 1

print(res)

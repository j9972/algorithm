steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]

data = input()

c = int(ord(data[0]) - ord('a'))  # a
r = int(data[1]) - 1  # 1, 1부터 시작하니까 2차원 배열에 맞게 -1 을 해서 0으로 맞춘다
cnt = 0


for s in steps:
    next_c = c + s[1]
    next_r = r + s[0]
    if 0 <= next_r < 8 and 0 <= next_c < 8:
        cnt += 1
print(cnt)

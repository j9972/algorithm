s = input()

s_list = list(s)

count = int(s_list[0])

for i in range(1, len(s_list)):
    if s_list[i] == '0' or count == 0:
        count += int(s_list[i])
    else:
        count *= int(s_list[i])

print(count)

# new way -> 데이터가 1일때는 더하는게 더 좋다
# data = list(map(int, input()))
# ans = data[0]

# print("data = {}".format(data))

# for i in range(1, len(data)):
#     if ans == 0 or data[i] == 0 or data[i] == 1:
#         ans += data[i]
#     else:
#         ans *= data[i]


# print(ans)

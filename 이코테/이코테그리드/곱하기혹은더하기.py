s = input()

s_list = list(s)

count = int(s_list[0])

for i in range(1, len(s_list)):
    if s_list[i] == '0' or count == 0:
        count += int(s_list[i])
    else:
        count *= int(s_list[i])

print(count)

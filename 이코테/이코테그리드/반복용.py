data = list(map(int, input()))
ans = data[0]

print("data = {}".format(data))

for i in range(1, len(data)):
    if ans == 0 or data[i] == 0 or data[i] == 1:
        ans += data[i]
    else:
        ans *= data[i]


print(ans)

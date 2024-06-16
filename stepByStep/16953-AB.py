a,b = map(int,input().split())

min_val = 0
flag = False

while not flag:

    if b % 10 == 1:
        b = int(str(b)[:-1])
        min_val += 1
    elif b % 2 == 0:
        b //= 2
        min_val += 1
    else:
        flag = True
        break

    if a > b:
        flag = True
        break

    if a == b:
        min_val += 1
        break


if flag:
    print(-1)
else:
    print(min_val)
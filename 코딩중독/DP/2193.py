n = int(input())
d = [0 for _ in range(91)]

for i in range(1, n+1):
    if i == 1:
        d[i] = 1
    elif i == 2:
        d[i] = 1
    else:
        d[i] = d[i-2] + d[i-1]


print(d[n])

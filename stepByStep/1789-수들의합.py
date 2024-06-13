s = int(input())

idx = 0

while s >= idx:
    s -= idx
    idx += 1

print(idx-1)
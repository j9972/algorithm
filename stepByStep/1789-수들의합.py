s = int(input())

max_val = 0
idx = 1

while s > idx:
    s -= idx
    idx += 1

print(idx-1)
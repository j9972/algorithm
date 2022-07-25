n, k = map(int, input().split())

count = 0

while True:
    if n % k == 0:
        count += 1
        n //= k
        if n == 1:
            break
    else:
        count += 1
        n -= 1
        if n == 1:
            break

print(count)

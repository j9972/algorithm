import sys
input = sys.stdin.readline

n = int(input())
price = list(map(int, input().split()))
m = int(input())

res = [0]
priceMin = float('int')
priceMinNum = 0

for i in range(1, n):
    if price[i] <= priceMin:
        priceMin = price[i]
        priceMinNum = i

if priceMin > m:
    print('0')
    exit(0)

res[0] = priceMinNum
m -= priceMin

if price[0] < priceMin:
    priceMin = price[0]
    priceMinNum = 0

res += [priceMinNum for _ in range(m//priceMin)]
remain = m % priceMin

# 1번째 자리
if remain != 0:
    for i in range(n-1, res[0], -1):
        if remain >= price[i] - price[res[0]]:
            remain -= (price[i] - price[res[0]])
            res[0] = i
            break

for i in range(1, len(res)):
    if remain == 0:
        break
    for j in range(n-1, priceMinNum, -1):
        if remain >= price[j] - priceMin:
            res[i] = j
            remain -= (price[j] - priceMin)
            break
print(''.join(map(str, res)))

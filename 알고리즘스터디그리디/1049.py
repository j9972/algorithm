import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

brand = []
for i in range(m):
    brand.append(list(map(int, input().split())))

money = []

for i in range(len(brand)):
    res = 0
    if n // 6 == 0:
        if brand[i][0] > n * brand[i][1]:
            res = n * brand[i][1]
            money.append(res)
        else:
            res = brand[i][0]
            money.append(res)
    else:
        if (n//6) * brand[i][0] + (n % 6) * brand[i][1] > n * brand[i][1]:
            res = n * brand[i][1]
            money.append(res)
        else:
            res += (n // 6) * brand[i][0]
            res += (n % 6) * brand[i][1]
            money.append(res)

print("money: {}".format(money))

print(min(money))

n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]

ans = 0
if m % (k+1) == 0:
    ans = (first * k + second) * (m // (k+1))
else:
    ans = (first * k + second) * (m // (k+1)) + first * (m % (k+1))
print(ans)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = list()
for i in range(n):
    data.append(int(input()))

count = 0

data.sort(reverse=True)

for i in data:
    if k >= i:
        count += k // i
        k %= i
        if k <= 0:
            break


print(count)

# 이렇게 하려고 했는데 이렇게 하면 k값과 같은 값이 원소로 있을때 등과 같은 체크할점들이 많아진다.
# while k > 0:
#     data.append(k)
#     data.sort()

#     for i in range(len(data)):
#         if data[i] == k:
#             count += k // data[i-1]
#             k -= (k // data[i-1]) * data[i-1]

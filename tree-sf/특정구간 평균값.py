n = int(input())
arr = list(map(int,input().split()))

cnt = 0

# 1번
# for i in range(1,n+1):
#     for j in range(n - i + 1):

#         avg = sum(arr[j:j+i]) / i

#         if avg in arr[j:j+i]:
#             cnt += 1
# print(cnt)

# 2번
for i in range(n):
    for j in range(i,n):

        val = sum(arr[i:j+1])

        avg = val / (j - i + 1)

        if avg in arr[i:j+1]:
            cnt += 1
print(cnt)



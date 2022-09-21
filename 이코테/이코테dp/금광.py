# 왼쪽 위, 왼쪽 아래, 왼쪽에서 오는 경우만 있음

# t = int(input())

# for tc in range(t):
#     n, m = map(int, input().split())
#     data = list(map(int, input().split()))

#     dp = []
#     idx = 0
#     for i in range(n):
#         dp.append(data[idx:idx+m])
#         idx += m

#     for j in range(1, m+1):
#         for i in range(n):
#             # left up
#             if i == 0:  # 범위 끝
#                 left_up = 0
#             else:
#                 left_up = dp[i-1][j-1]

#             # left down
#             if i == n - 1:
#                 left_down = 0
#             else:
#                 left_down = dp[i+1][j-1]

#             # left
#             left = dp[i][j-1]

#             dp[i][j] += max(left_up, left_down, left)

# res = 0
# for i in range(n):
#     res = max(res, dp[i][m-1])

# print(res)

for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index: index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]
            dp[i][j] += max(left_up, left_down, left)

result = 0
for i in range(n):
    result = max(result, dp[i][m - 1])
print(result)

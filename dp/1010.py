# 다리 놓기
import sys
input = sys.stdin.readline


# def fact(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


# for tc in range(int(input())):
#     # 서쪽 -- 동쪽 사이트의 개수
#     westBridge, eastBridge = map(int, input().split())

#     bridge = fact(eastBridge) // (fact(eastBridge -
#                                        westBridge) * fact(westBridge))

#     print(bridge)

for tc in range(int(input())):
    west, east = map(int, input().split())
    dp = [[0 for _ in range(east+1)] for _ in range(west+1)]

    for i in range(1, west+1):
        for j in range(1, east+1):
            if i == 1:
                dp[i][j] = j
                continue
            if i == j:
                dp[i][j] = 1
            else:
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[west][east])

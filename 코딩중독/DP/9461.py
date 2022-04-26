import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())

    dp = [0 for i in range(101)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, 101):
        dp[i] = dp[i-3] + dp[i-2]

    for i in range(t):
        n = int(input())
        print(dp[n])

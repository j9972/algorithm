import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    a = [0] + list(map(int, input().split()))

    dp = [0 for i in range(n+1)]

    for i in range(1, n+1):
        for k in range(1, i+1):
            dp[i] = max(dp[i], dp[i-k]+a[k])

    print(dp[n])

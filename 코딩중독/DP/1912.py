import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * len(a)
    dp[0] = a[0]

    for i in range(1, len(a)):
        dp[i] = max(a[i], dp[i-1]+a[i])

    print(max(dp))

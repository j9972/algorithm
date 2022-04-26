import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = list(str(input().strip()))
    l = len(n)
    dp = [0 for _ in range(l+1)]
    dp[0], dp[1] = 1, 1

    if n[0] == '0':
        print(0)
    else:
        for i in range(2, l+1):
            if int(n[i-1]) > 0:
                dp[i] += dp[i-1]
            tmp = int(n[i-2] + n[i-1])
            if 10 <= tmp <= 26:
                dp[i] += dp[i-2]

        print(dp[l] % 1000000)

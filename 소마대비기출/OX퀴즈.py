# 브2 - 8958
import sys
input = sys.stdin.readline


for tc in range(int(input())):
    s = input().rstrip()
    n = len(s)
    d = [0] * (n+1)

    if s[0] == 'O':
        d[0] = 1
    else:
        d[0] = 0

    for i in range(1, n):
        if s[i] == 'O':
            if d[i-1] != 0:
                d[i] = d[i-1] + 1
            else:
                d[i] = 1
        else:
            d[i] = 0
    res = 0
    for i in range(n):
        res += d[i]
    print(res)

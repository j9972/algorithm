# 실버 3 - 9461
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())

    d = [0] * 101
    d[1] = 1
    d[2] = 1
    d[3] = 1
    for i in range(4, n+1):
        d[i] = d[i-3] + d[i-2]

    print(d[n])

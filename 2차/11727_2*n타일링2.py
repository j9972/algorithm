import sys
input = sys.stdin.readline

d = [0] * 1001
d[0] = 0
d[1] = 1
d[2] = 3
d[3] = 5
d[4] = 11

n = int(input())

if n >= 5:
    for i in range(5, n+1):
        d[i] = d[i-1] + d[i-2] * 2

print(d[n]%10007)
# 다시 부분
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
data = [0]
for i in range(n):
    data.append(int(input()))

if n == 1:
    print(data[1])
else:
    d = [0] * (n+1)
    d[0] = 0
    d[1] = data[1]
    d[2] = data[1] + data[2]

    for i in range(3, n+1):
        d[i] = max(d[i-3] + data[i-1], d[i-2]) + data[i]
    print(d[n])

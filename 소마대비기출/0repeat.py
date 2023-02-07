# 다시 부분
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
data = list(map(int, input().split()))
d = [0] * n
d[0] = data[0]
for i in range(1, n):
    d[i] = max(data[i], d[i-1] + data[i])
print(max(d))

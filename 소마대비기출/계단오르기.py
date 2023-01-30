# 실버3
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.reverse()
ans = data[0]

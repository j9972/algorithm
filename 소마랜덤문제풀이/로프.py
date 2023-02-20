# 실버 4 - 2217
import sys
input = sys.stdin.readline

n = int(input())
weight = []
for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)

mv = 0
for i in range(n):
    if mv < weight[i]*(i+1):
        mv = weight[i]*(i+1)
print(mv)

# 안테나
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

print(data[(n-1) // 2])

# 실버 1 - 11052
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
price = []
for i in range(len(data)):
    price.append([data[i], i+1])  # 카드값, 카드개수

ans = 0

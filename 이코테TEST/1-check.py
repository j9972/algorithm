from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

maxCoin = 1
for c in coin:
    if maxCoin < c:
        break
    maxCoin += c
print(maxCoin)

import sys
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

maxCoin = 1
for i in coin:
    if maxCoin < i:
        break
    maxCoin += i

print(maxCoin)

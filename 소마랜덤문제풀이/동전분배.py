#골드3 - 1943
import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    coin = []
    for i in range(n):
        price,cnt = map(int,input().split())
        coin.append((price,cnt))
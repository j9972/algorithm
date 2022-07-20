# keep
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

for i in range(n):
    price = list(map(int, input().split()))

m = int(input())

roomNum = []

while m > 0:
    if m > price[-1]:
        roomNum.append(price[-1])

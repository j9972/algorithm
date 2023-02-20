# 실버 3 - 13305
import sys
input = sys.stdin.readline

node = int(input())

road = list(map(int,input().split())) # n-1
cost = list(map(int,input().split())) # n

minPrice = cost[0] * road[0]

minCost = cost[0]
for i in range(1,node-1):
    if cost[i] < minCost:
        minCost = cost[i]
    minPrice += minCost * road[i]
print(minPrice)
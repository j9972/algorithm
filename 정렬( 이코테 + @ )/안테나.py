import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int,input().split()))

print(distance[n//2 - 1])
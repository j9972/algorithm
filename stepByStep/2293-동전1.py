import sys
sys.setrecursionlimit(10**7)

n,k = map(int,input().split())

coin = [
    int(input())
    for _ in range(n)
]

d = [0] * (k+1)
d[0] = 1

for i in coin:
    for j in range(1,k+1):
        if j - i >= 0:
            d[j] += d[j-i]
print(max(d))
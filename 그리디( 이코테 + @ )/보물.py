import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))
a.sort()

b = list(map(int,input().split()))
b.sort(reverse=True)

res = 0
for i in range(n):
    res += (a[i] * b[i])
print(res)
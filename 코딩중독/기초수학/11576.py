import sys
input = sys.stdin.readline

n, b = map(int, input().split())
t = int(input())
arr = list(map(int, input().split))
a = 0

for i in range(t):
    a += arr[t-i-1] * n ** i

ans = ''

while a:
    ans = ' ' + ans
    ans = str(a % b) + ans
    a //= b

print(ans)

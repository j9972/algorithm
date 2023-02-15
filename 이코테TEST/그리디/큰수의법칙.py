import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
f = data[0]
s = data[1]
ans = 0

ans += m % (k+1) * f + m//(k+1) * (f*k+s)
print(ans)

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort(reverse=True)

ans = 0
if m // (k+1) > 0:
    ans += (data[0] * k + data[1]) * (m//(k+1))
else:
    if m % (k+1) != 0:
        ans += data[0] * (m%(k+1))

print(ans)

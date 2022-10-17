# 큰 수의 법칙
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data = sorted(data, reverse=True)
count = 0

ans = 0

# 가장 큰수가 2개일때 -> m * 큰수
if data[0] == data[1]:
    ans += m * data[0]

# 가장 큰수가 1개일때 ->  while ( k * 큰수 + 2번째 큰수 <= m )
if data[0] != data[1]:
    while m > 0:
        ans += data[0]
        m -= 1
        count += 1
        if count == k:
            ans += data[1]
            m -= 1
            count = 0

print(ans)

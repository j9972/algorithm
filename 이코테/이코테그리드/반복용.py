# 숫자 카드 게임
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = 0

for i in range(n):
    data = map(int, input().split())

    minValue = min(data)

    ans = max(ans, minValue)

print(ans)

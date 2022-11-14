# 숫자 카드 게임
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

res = []
for i in range(n):
    res.append(min(data[i]))
print(max(res))

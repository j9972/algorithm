# 효율적인 화폐 구성
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

# 결국에 최소한의 개수의 화폐로 m원을 맞춰야 하므로 이렇게 초기화 하는 것이 맞다
d = [10001] * (m+1)

# 0원을 만드는데는 0번이면 된다
d[0] = 0
for i in range(n):
    for j in range(data[i], m+1):
        # m원을 맞출 수 있다면
        if d[j-data[i]] != 10001:
            d[j] = min(d[j], d[j-data[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

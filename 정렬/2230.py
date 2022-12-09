# 수고르기 -> 조합은메모리 초과, 투포인터로 풀기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()


def check(data):
    s, e = 0, 1
    ans = 10e9

    while e < n:
        if data[e] - data[s] == m:
            return m
        if data[e] - data[s] < m:
            e += 1
            continue
        ans = min(ans, data[e] - data[s])
        s += 1
    return ans


print(check(data))

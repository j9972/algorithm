# 아직 미완성 - 부분합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())

data = list(map(int, input().split()))

interval_sum = 0
value = 0
count = 0
res = []
end = 0

for i in range(n-1):
    if data[i] <= data[i+1]:
        while interval_sum < s and end < n:
            interval_sum += data[end]
            value += 1
            end += 1

        if interval_sum >= s:
            count += 1
            res.append(value)
        interval_sum -= data[i]
        value -= 1

print(len(res))

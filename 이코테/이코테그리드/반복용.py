n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

f = data[0]
s = data[1]

# 가장 큰수가 더해지는 횟수 계산 -> k만큼 반복 될수있으니까 곱해야한다
count = int(m/(k+1)) * k + m%(k+1)

res = 0
res += count * f
res += (m-count) * s

print(res)



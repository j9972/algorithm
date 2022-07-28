n = int(input())

t = list(map(int, input().split()))

t.sort()

sumN = []

for i in range(len(t)):
    sumN.append(t[i]*(n-i))


print(sum(sumN))

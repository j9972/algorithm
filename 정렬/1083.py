import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
    maxValue = data[i]
    val = 0

    if s == 0:
        break

    for j in range(i+1, n):
        gap = j - i
        if maxValue <= data[j]:
            maxValue = data[j]
            val = gap
        if gap >= s:
            break

    if val != 0:
        s -= val
        data.remove(maxValue)
        data.insert(i, maxValue)

print(*data)

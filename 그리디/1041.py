import sys
input = sys.stdin.readline

# 주사위 갯수 n^3
n = int(input())
data = list(map(int, input().split()))

if n == 1:
    print(sum(data)-max(data))
else:
    res = [min(data[0], data[5]), min(data[1], data[4]), min(data[2], data[3])]
    res.sort()
    first = (5*(n**2) - 8*n + 4) * res[0]
    second = (8*n - 8) * res[1]
    third = 4 * res[2]

    print(first+second+third)

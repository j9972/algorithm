# 금광
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    data = []
    index = 0
    for i in range(n):
        data.append(arr[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = data[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = data[i+1][j-1]

            left = data[i][j-1]

            data[i][j] += max(left, left_down, left_up)

    res = 0
    for i in data:
        res = max(res, max(i))
    print(res)

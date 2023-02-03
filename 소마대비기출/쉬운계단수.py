# 실버 1 - 10844 - 다시
import sys
input = sys.stdin.readline

n = int(input())

d = [[0] * 10 for _ in range(n+1)]

d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    d[i][0] = d[i-1][1]  # 0 뒤에는 1밖에 못옴
    d[i][9] = d[i-1][8]  # 9 앞애는 8밖에 못옴

    for j in range(1, 9):
        d[i][j] = d[i-1][j-1] + d[i-1][j+1]


print(sum(d[n]) % 1000000000)

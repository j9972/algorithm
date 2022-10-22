# RGB 거리
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# 처음 시작하는 최솟값 찾기 -> 2차원 배열의 열파트는 rgb 3가지 밖에 없다
for i in range(1, len(data)):
    data[i][0] += min(data[i-1][1], data[i-1][2])
    data[i][1] += min(data[i-1][0], data[i-1][2])
    data[i][2] += min(data[i-1][1], data[i-1][0])

print(min(data[n-1][0], data[n-1][1], data[n-1][2]))

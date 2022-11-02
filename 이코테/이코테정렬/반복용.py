# 성적이 낮은 순서로 학생 출력하기
import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    data.append(list(input().split()))

dataArr = sorted(data, key=lambda x: int(x[1]))

for i in dataArr:
    print(i[0], end=' ')

# 1337 실버4
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()

maxVal = 0
for i in range(n):
    cnt = 0
    res = []
    for j in range(data[i]+1,data[i]+5):
        res.append(j)
    
    for d in data:
        if d in res:
            cnt += 1
    
    if cnt > maxVal:
        maxVal = cnt
print(4-maxVal)
#data의 모든 원소들을 기준으로 +4까지 전부 체크해서 그 안에 들어오는 data의 개수 체크해서 가장 많은거 고르기

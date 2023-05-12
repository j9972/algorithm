# 1138 실버2
import sys
input = sys.stdin.readline

n = int(input())
order = list(map(int,input().split()))

res = []
#print(res)
for i in range(n-1,-1,-1):
    #order[i]의 값을 res의 인덱스값으로 생각해서 데이터 넣어주기
    res.insert(order[i], i+1)

for i in res:
    print(i,end=' ')
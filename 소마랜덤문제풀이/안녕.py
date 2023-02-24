# 실버2 - 1535
import sys
input = sys.stdin.readline

n = int(input())
power = [0] + list(map(int,input().split()))
happy = [0] + list(map(int,input().split()))

d = [[0] * (101) for _ in range(n+1)]
for i in range(n+1): # 모두 돌아가디니면서 보기
    for j in range(1,101):
        if power[i] <= j: # 감당 가능
            d[i][j] = max(d[i-1][j], d[i-1][j-power[i]] + happy[i])
        else: # 감당 불가
            d[i][j] = d[i-1][j]


print(d[n][99]) # power의 마지노선은 99

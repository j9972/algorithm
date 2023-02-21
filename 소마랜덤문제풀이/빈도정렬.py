# 실버2 - 2910
import sys
input = sys.stdin.readline

n,maxValue = map(int,input().split())
nums = list(map(int,input().split()))

dic = dict()
for i in nums:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

dic = sorted(dic.items(), key=lambda x:x[1], reverse=True )

for a,b in dic:
    for i in range(b):
        print(a, end=' ')
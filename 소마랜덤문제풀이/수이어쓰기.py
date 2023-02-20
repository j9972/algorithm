# 실버 3 1515 -> 버리자
import sys
input = sys.stdin.readline

n = input()
i = 0

while True:
    i+=1 
    num = str(i)
    if len(num) > 0 and len(n) > 0:
        if num[0] == n[0]:
            n = n[1:]
        num = num[1:]
        #print(num)# 
    if n == '':
        print(i)
        break

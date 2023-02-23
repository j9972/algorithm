# 실버4 - 2870
import sys
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    s = input().rstrip()
    cnt = ""
    

    for i in s:
        if ord(i) < 97:
            cnt += i
        else:
            if cnt:
                res.append(int(cnt))
                cnt = ""
    if cnt:
        res.append(int(cnt))
    
        
res.sort()
for i in res:
    print(i)

# 1790 골5
import sys
input = sys.stdin.readline

n,k = map(str,input().split())

cnt = 0

def finding(n):
    global cnt
    for i in range(1,n+1):
        cnt += 9 * i * (10 ** (i-1))
    return cnt

data = finding(len(n))

if data < int(k):
    print(-1)
else:
    for i in range(1,len(n)+1):
        check = 9 * i * (10 ** (i-1))
        if int(k)  <= data:
            # i자리수값이다.
            res = ''
            pnt = '1' + '0'* (i-1)
            kkk = int(k) - (data - check)
            for j in range(int(pnt),int(pnt) + kkk + 1):
                if kkk == 0:
                    break
                for h in str(j):
                    res += h
                    kkk -= 1
                    if kkk == 0:
                        break
    print(res[-1])
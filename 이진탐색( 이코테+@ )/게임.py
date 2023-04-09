import sys
input = sys.stdin.readline

x,y = map(int,input().split())

z = (100*y)//x

res = x
start = 1
end = x

if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start+end) // 2 # 특정 횟수만큼 더해졌을떄 z가 변하는지 체크 

        if (y+mid) * 100 // (x+mid) > z:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    print(res)

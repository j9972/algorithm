# test case 7 ~ 10 시간 초과
def solution(r1, r2):
    cnt = 0

    for x in range(r2):
        for y in range(r2):
            if (x != 0 and y != 0) and ( r1**2 <= x**2 + y**2 <= r2**2):
                cnt += 1
    
    return 4*(cnt+r2-r1+1)

def solution(r1, r2):
    ans = 0
    minY , maxY = r1, r2
    for x in range(r2):
        while r2 ** 2 < maxY**2 + x**2:
            maxY -= 1
            
        # 최소값 양수 유지
        while minY-1 and r1**2 <= (minY-1)** 2 + x**2:
            minY -= 1
            
        ans += (maxY-minY+1)
        
    return 4*ans
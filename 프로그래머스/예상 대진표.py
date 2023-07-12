# 1개의 방법
import math
def solution(n,a,b):
    a, b = min(a,b), max(a,b)
    for k in range(1, int(math.log2(n))+1):
        if a%2 != 0 and a+1 == b: 
            return k
        else:
            n, a, b = n/2, math.ceil(a/2), math.ceil(b/2)

# 2번째 방법
import math

def solution(n,a,b):
    ans = 0 
    while True:
        
        if a == b:
            break
        
        ans += 1
        a,b = (a+1)//2, (b+1)//2
        
    return ans

# 틀렸던 내 방법
import math

def solution(n,a,b):
    maxCnt = int(math.log2(n))
    
    while abs(a-b) > 1:
            
        if (a <= (n //2) and b <= (n//2)) or (a > (n //2) and b > (n//2)): # n//2 기준으로 왼쪽 혹은 오른쪽 어느쪽에 분포된지 확인하기 위함
            maxCnt -= 1
            if a % 2 == 1: 
                a += 1
            if b % 2 == 1:
                b += 1
            a //= 2
            b //= 2

        else:
            break
            
        n //= 2 
        
        
    return maxCnt
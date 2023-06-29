def checkNum(n):
    if n % 2 == 0:
        return True
    else:
        return False

def solution(n):
    ans = 0
    
    if n == 1:
        return 1
    
    while True:
        if checkNum(n):
            n //= 2
        else:
            n -= 1
            ans += 1
        
        if n == 2:
            ans += 1
            break
        if n == 1:
            break
            

    return ans
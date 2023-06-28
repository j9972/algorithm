# LV -2 
from itertools import permutations as pm
def prime(n):
    if n < 2:                                 
        return False
            
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    ans = 0
    res = []
    n = []
    
    for i in numbers:
        n.append(i)
    
    for i in range(1,len(n)+1):
        for j in list(pm(n,i)):
            data = ''.join(j)
            if (int(data) not in res) and int(data) != 0:
                res.append(int(data))
    
    for data in res:
        if prime(data) == True:
            ans += 1
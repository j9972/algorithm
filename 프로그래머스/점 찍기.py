import math

def solution(k, d):
    answer = 0 
    
    if k > d:
        return 1
    elif k == d:
        return 3
    else:
        for i in range(0,d+1,k):
                answer += math.floor(math.floor( math.sqrt(d**2 - (i**2)) ) /k) + 1
    
        return answer
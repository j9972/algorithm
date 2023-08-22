# 시간 초과 
from itertools import permutations as pm
# def solution(n, k):
#     data = [i for i in range(1,n+1)]
    
#     res = list(pm(data,n))
    
#     return res[k-1]

def solution(n, k):
    res = []
    data = [i for i in range(1,n+1)]

    d = [1] * (n+1)
    d[1] = 1

    for i in range(2, n+1):
	    d[i] = d[i-1] * i
    
    #print(d)
    
    while n > 0:
        val = (k-1) // d[n-1]
        res.append(data[val])
        del data[val]

        k = k % d[n-1]
        n -= 1
    
    print(res)
solution(3, 5)

def solution(n, k):
    res = []
    data = [i for i in range(1,n+1)]

    # fact를 dp로 표현
    d = [1] * (n+1)
    d[1] = 1

    for i in range(2, n+1):
	    d[i] = d[i-1] * i
    
    while n > 0:
        res.append(data[(k-1) // d[n-1]])
        data.remove(data[(k-1) // d[n-1]])

        k = k % d[n-1]
        n -= 1
    
    return res

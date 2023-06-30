from collections import deque
def solution(people, limit):
    
    res = 0
    people.sort(reverse = True)
    dq = deque(people)
    
    while dq:
        a = limit - dq.popleft()
        
        while dq and dq[-1] <= a:
            a -= dq.pop()
        res += 1
        
    return res
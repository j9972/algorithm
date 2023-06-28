from collections import deque
def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for p in range(len(priorities)):
        if p == location:
            q.append([priorities[p], True])        
        q.append([priorities[p], False])
    
    check = False
    
    while True:
        prior, flag = q.popleft()
        
        for p,f in q:
            if p > prior:
                q.append([prior, flag])
                check = True
                break
            else:
                continue
        
        if check == False:
            answer += 1
            if flag == True:
                break
        
        check = False
        
    return answer
# test case 20 ~ 23까지 시간 초과
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        flag = False
        
        for j in range(i+1,len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                flag = True
                break
                
        if flag == False:
            answer.append(-1)
            
    answer.append(-1)      
            
    
    return answer

# test case 20 ~ 23까지 시간 초과  
def solution(numbers):
    ans = []
    
    i = 0
    while True: 
        
        if i == len(numbers):
            break
        
        flag = False
        for j in range(i+1,len(numbers)):
            if numbers[j] > numbers[i]:
                ans.append(numbers[j])
                flag = True
                break
                
        if flag == False:    
            ans.append(-1)
        i += 1
    return ans

# test case 20 ~ 23까지 시간 초과  
from collections import deque
def solution(numbers):
    answer = []
    
    q = deque(numbers)
    
    i = 0
    while q:
        value = q.popleft()
        
        flag = False
        for j in range(i+1,len(numbers)):
            if value < numbers[j]:
                answer.append(numbers[j])
                flag = True
                break
        if flag == False:
            answer.append(-1)
        i+=1
    
    return answer

# 구글링으로 알아낸 stack 을 이용한 방법
def solution(numbers):
    
    n = len(numbers)
    
    answer = [-1] * n
    st = []
    
    for index in range(n):
        
        value = numbers[index]
        
        while st and numbers[st[-1]] < value:
            answer[st.pop()] = value
        
        st.append(index)
    
    return answer

# 우선 순위 큐
from heapq import *

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n

    h = []

    for i in range(n):
        value = numbers[i]

        while h and h[0][0] < value:
            _, idx = heappop(h)
            answer[idx] = value

        heappush(h, [value, i])

    return answer
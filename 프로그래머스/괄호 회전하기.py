from collections import deque
def balance(s):
    st = []
    for i in s:
        if i == '(' or i == '{' or i =='[':
            st.append(i)
        elif st and i == ')' and st[-1] == '(':
            st.pop()
        elif st and i == '}' and st[-1] == '{':
            st.pop()
        elif st and i == ']' and st[-1] == '[':
            st.pop()            
        else:
            return False
    
    if len(st) == 0:
        return True
    
    return False
            

def solution(s):
    ans = 0
    q = deque(s)
    
    for _ in range(len(s)):
        if balance(q) == True:
            ans += 1
        q.append(q.popleft())
    
    return ans
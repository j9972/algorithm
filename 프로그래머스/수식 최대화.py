from itertools import permutations as pm
from collections import deque

def cal(a,b,oper):
    if oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '+':
        return a + b

def solution(expression):
    
    st = []
    for e in expression:
        if (e in ['-', '*', '+']) and e not in st:
            st.append(e)
    
    # 우선순위 나오는 경우의 수
    express = list(pm(st,len(st)))
    
    ans = 0
    for i in express:
        expressions = []
        val = ''
        for ex in expression:
            if ex not in ['-', '*', '+']:
                val += ex
            else:
                expressions.append(int(val))
                expressions.append(ex)
                val = ''
    
        if val != '':
            expressions.append(int(val))
        
        for op in i:
            print("op :", op)
            q = deque(expressions)
            print("q :", q)
            tk = []
        
            while q:
                data = q.popleft()
                print("data :",data)
                if data == op:
                    last = tk.pop()
                    val = q.popleft()
                    print("last {} val {} op {}".format(last, val, op))
                    tk.append(cal(last,val,op))
                else:
                    tk.append(data)
                print("tk :", tk)
            expressions = tk
        
        res = abs(expressions[0])
        print(res)
        ans = max(res,ans)
    return ans
    
    
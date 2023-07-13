# 시간 초과
# def solution(topping):
#     ans = 0
    
#     st = []
    
#     for t in range(len(topping)):
#         if topping[t] not in st:
#             st.append(topping[t])
#         if len(st) == len(set(topping[t+1:])):
#             ans += 1

#     return ans

from collections import Counter
def solution(topping):
    ans = 0
    
    bro = Counter(topping)
    me = set()
    
    for i in topping:
        bro[i] -= 1
        if bro[i] == 0:
            del bro[i]
        me.add(i)
        
        if len(me) == len(bro):
            ans += 1
    return ans
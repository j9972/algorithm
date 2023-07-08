def solution(clothes):
    ans = 1
    
    dic = dict()
    
#     for cloth in clothes:
#         name, typ = cloth
        
#         if typ in dic:
#             dic[typ] += 1
#         else:
#             dic[typ] = 1

    for _, typ in clothes:
        
        if typ in dic:
            dic[typ] += 1
        else:
            dic[typ] = 1
        
    print(dic)
    
    for h in dic.values():
        ans *= (h+1)
        #print("{} {}".format(h, ans))
            
    return ans - 1
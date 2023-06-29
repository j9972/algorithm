def solution(s):
    ans = []
    
    dic ={}
    s = s.replace('{','')
    s = s.replace('}','')
    s = list(s.split(','))

    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for data in sorted(dic,key=lambda x:dic[x], reverse=True):
        ans.append(int(data))
    
    return ans


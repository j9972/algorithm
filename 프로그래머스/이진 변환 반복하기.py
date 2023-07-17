def solution(s):
    answer = []
    cnt = 0
    zero = 0
    
    while s != '1':
        zero += s.count("0")
        s = s.replace("0","")
        c = len(s)
        s = bin(c)[2:]
        cnt += 1 

    answer.append([cnt,zero])
        
    return answer[0]
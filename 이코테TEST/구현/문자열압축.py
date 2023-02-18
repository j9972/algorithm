def solution(s):
    ans = len(s)
    for step in range(1,len(s)//2+1):
        cnt = 1
        prev = s[:step]
        compression = ""
        
        for i in range(step,len(s),step):
            if s[i:i+step] == prev:
                cnt += 1
            else:
                compression += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = s[i:step+i]
        compression += str(cnt) + prev if cnt >= 2 else prev
        ans = min(ans, len(compression))
    
    return ans
import math
def solution(w,h):
    answer = 1
    
    if (w == 1 or h == 1):
        return 0
    
    if w == h:
        return w * h - h
    else:
        g = math.gcd(w,h)
        
        ww = w // g
        hh = h // g
        
        cut = (ww*hh) - ((ww-1) * (hh-1))
        answer = w * h - (cut * g)
        
        return answer
import sys
input = sys.stdin.readline

def balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
def proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            else:
                count -= 1
    return True

def sol(p):
    ans = ""
    if p == "":
        return ""
    
    idx = balance(p)
    v = p[idx+1:]
    u = p[:idx+1]

    if proper(p):
        ans = u + sol(v)
    else:
        ans += '('
        ans += sol(v)
        ans += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        ans += ''.join(u)
    return ans

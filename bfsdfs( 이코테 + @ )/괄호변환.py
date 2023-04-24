def balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

def proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            else:
                cnt -= 1
    return True

def sol(p):
    ans = ''
    if p == '':
        return ans
    idx = balance(p)
    u = p[:idx+1]
    v = p[idx+1:]


    if proper(u):
        ans = u + sol(v)
    else:
        ans += '('
        ans += sol(v)
        ans += ')'

        u_list = list(u[1:-1])
        for i in range(len(u_list)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        ans += ''.join(u_list)
    return ans

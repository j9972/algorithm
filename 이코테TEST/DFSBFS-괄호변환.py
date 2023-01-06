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


def solution(p):
    ans = ''
    if p == '':
        return ans

    idx = balance(p)
    v = p[idx+1:]
    u = p[:idx+1]

    if proper(u):
        ans = u + solution(v)
    else:
        ans += '('
        ans += solution(v)
        ans += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        ans += ''.join(u)
    return ans


p = "()))((()"
print(solution(p))

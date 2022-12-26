# balance
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


def solution(p):
    ans = ''
    if p == '':
        return ans
    idx = balance(p)
    # u는 더이상 분리 할수 없다고 하니 balance로 되는 부분까지를 말함
    u = p[:idx+1]
    # 빈배열도 가능하다고 하니까 뒤의 나머지 p들을 의미 한다
    v = p[idx+1:]
    if proper(u):
        # 올바른 문자열이면 u 뒤에 v에 대해 1단계 부터 다시 수행한다고 하니까 이어 붙이면 된다.
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


def solution(p):
    ans = ' '
    if not p:
        return p

    res, cnt = True, 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt -= 1
        else:
            cnt += 1

        if cnt > 0:
            res = False     # 올바른 괄호 문자열아 아니다.

        u = p[:i+1]
        v = p[i+1:]

        if cnt == 0:
            if res:
                ans = u + solution(v)
            else:
                ans += '(' + solution(v) + ')'
                u = list(u[1:-1])
                for i in range(len(u)):
                    if u[i] == '(':
                        u[i] = ')'
                    else:
                        u[i] = '('
                ans += ''.join(u)
            return ans
    #ans += ''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))

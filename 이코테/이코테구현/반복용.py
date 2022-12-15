def possible(ans):
    for x, y, a in ans:
        if a == 0:
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            return False

        elif a == 1:
            if ([x-1, y, 1] in ans and [x+1, y, 1] in ans) or [x, y-1, 0] in ans or [x+1, y-1, 0] in ans:
                continue
            return False
    return True


def solution(n, bf):
    ans = []
    for f in bf:
        x, y, a, oper = f
        if oper == 0:
            ans.remove([x, y, a])
            if not possible(ans):
                ans.append([x, y, a])
        elif oper == 1:
            ans.append([x, y, a])
            if not possible(ans):
                ans.remove([x, y, a])
    return sorted(ans)

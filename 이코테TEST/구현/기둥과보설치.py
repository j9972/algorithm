def check(arr):
    for x, y, a in arr:
        if a == 0:  # 기둥
            if y == 0 or [x, y-1, 0] in arr or [x-1, y, 1] in arr or [x, y, 1] in arr:
                continue
            return False
        elif a == 1:  # 보
            if [x, y-1, 0] in arr or [x+1, y-1, 0] in arr or ([x-1, y, 1] in arr and [x+1, y, 1] in arr):
                continue
            return False
    return True


def solution(n, build_frame):
    res = []

    for i in build_frame:
        x, y, a, oper = i
        if oper == 0:  # 삭제
            res.remove([x, y, a])
            if not check(res):
                res.append([x, y, a])
        elif oper == 1:  # 설치
            res.append([x, y, a])
            if not check(res):
                res.remove([x, y, a])

    return sorted(res)

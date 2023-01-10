def satisfy(arr):
    for x, y, stuff in arr:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in arr or [x, y, 1] in arr or [x, y-1, 0] in arr:
                continue
            return False
        elif stuff == 1:
            if ([x-1, y, 1] in arr and [x+1, y, 1] in arr) or [x, y-1, 0] in arr or [x+1, y-1, 0] in arr:
                continue
            return False
    return True


def solution(n, build_frame):
    res = []

    for i in build_frame:
        x, y, frame, oper = i
        if oper == 0:  # 삭제인 경우
            res.remove([x, y, frame])
            if not satisfy(res):
                res.append([x, y, frame])
        if oper == 1:  # 삭제인 경우
            res.append([x, y, frame])
            if not satisfy(res):
                res.remove([x, y, frame])

    return sorted(res)
